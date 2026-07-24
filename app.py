from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
import logging
import traceback

# Load Environment Variables
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Read API Key
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    logger.error("GROQ_API_KEY not found in .env")
    raise ValueError("GROQ_API_KEY environment variable not set")

# Initialize Groq Client
try:
    client = Groq(api_key=API_KEY)
    logger.info("✅ Groq Client Initialized")
except Exception as e:
    logger.exception("Failed to initialize Groq client")
    client = None

# Available Models
SUPPORTED_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-120b"
]


@app.route("/")
def home():
    return render_template("index.html")


# Test API Endpoint
@app.route("/test_groq", methods=["GET"])
def test_groq():

    if not client:
        return jsonify({"ok": False, "error": "Groq client not initialized"}), 500

    try:
        response = client.chat.completions.create(
            model=SUPPORTED_MODELS[0],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Reply with only OK."
                }
            ],
            temperature=0,
            max_tokens=5
        )

        return jsonify({
            "ok": True,
            "model": SUPPORTED_MODELS[0],
            "response": response.choices[0].message.content
        })

    except Exception as e:
        logger.exception("Groq Test Failed")
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500


# Generate Blog
@app.route("/generate_blog", methods=["POST"])
def generate_blog():

    if not client:
        return jsonify({"error": "Groq client not initialized"}), 500

    topic = request.form.get("topic")
    tone = request.form.get("tone", "Professional")
    audience = request.form.get("audience", "General Audience")
    words = request.form.get("words", "1000")
    keywords = request.form.get("keywords", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    prompt = f"""
Write a high-quality SEO optimized blog.

Topic:
{topic}

Tone:
{tone}

Target Audience:
{audience}

Target Length:
Approximately {words} words

SEO Keywords:
{keywords}

Instructions:

- Create an engaging title.
- Write an attractive introduction.
- Use H2 and H3 headings.
- Explain every section clearly.
- Include examples wherever useful.
- Use bullet points where appropriate.
- Write in a human-friendly style.
- Optimize naturally for SEO.
- End with a conclusion.
- Add 5 FAQs.
- Finish with a meta description.
"""

    last_error = None

    for model in SUPPORTED_MODELS:

        try:

            logger.info(f"Trying Model: {model}")

            completion = client.chat.completions.create(

                model=model,

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert SEO content writer and professional blogger."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7,

                max_tokens=3500

            )

            blog = completion.choices[0].message.content

            # Save Blog

            os.makedirs("blogs", exist_ok=True)

            filename = f"blogs/blog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

            with open(filename, "w", encoding="utf-8") as file:
                file.write(blog)

            return jsonify({

                "success": True,

                "blog": blog,

                "model_used": model,

                "filename": filename

            })

        except Exception as e:

            logger.exception(f"Model {model} Failed")

            last_error = str(e)

            continue

    return jsonify({

        "success": False,

        "error": "All models failed",

        "details": last_error

    }), 500


if __name__ == "__main__":
    app.run(debug=True)