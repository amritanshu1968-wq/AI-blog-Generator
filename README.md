# 🚀 AI-Based Blog Generator

> Generate high-quality, SEO-optimized blog articles instantly using Artificial Intelligence.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Groq](https://img.shields.io/badge/Groq-AI-green)
![Render](https://img.shields.io/badge/Deployment-Render-success)

---

# 📌 Project Overview

The **AI-Based Blog Generator** is a web application developed as part of my **Internship & Training Program**. It leverages **Groq AI** and **Flask** to generate high-quality, SEO-friendly blog content within seconds.

Users simply enter a topic, select their preferred writing options, and the application automatically generates a professional blog complete with headings, FAQs, and a meta description.

---

# 🌐 Live Demo

**Website:** https://ai-based-blog-generator.onrender.com

---

# ✨ Features

- 🤖 AI-powered blog generation
- 📝 SEO-optimized content creation
- 🎯 Custom writing tone selection
- 👥 Audience-based content generation
- 📏 Adjustable blog length
- 🔑 SEO keyword support
- 📚 Automatic blog saving
- 📋 Copy generated content with one click
- 📥 Download blogs as `.txt` files
- 📖 Local blog history
- 🔄 Raw and formatted content views
- 📱 Fully responsive user interface
- ⚡ Fast content generation using Groq API

---

# 🛠 Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Font Awesome

## Backend
- Python
- Flask

## AI Integration
- Groq API

### Supported Models
- llama-3.3-70b-versatile
- llama-3.1-8b-instant
- openai/gpt-oss-120b

## Deployment
- Render

---

# 📂 Project Structure

```
AI-Based-Blog-Generator/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
├── blogs/
│   └── Generated Blog Files
│
├── static/
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Based-Blog-Generator.git
```

## 2. Navigate to the Project Folder

```bash
cd AI-Based-Blog-Generator
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create a `.env` File

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## 6. Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 🧠 How It Works

1. Enter the blog topic.
2. Select the desired tone.
3. Choose the target audience.
4. Specify the blog length.
5. Add SEO keywords (optional).
6. Submit the request.
7. Flask sends the prompt to the Groq API.
8. The AI generates a complete SEO-friendly blog.
9. The generated blog is displayed and automatically saved.
10. Users can copy, download, or revisit previous blogs.

---

# 🔄 Application Workflow

```
User
   │
   ▼
Frontend (HTML/CSS/JavaScript)
   │
   ▼
Flask Backend
   │
   ▼
Prompt Generation
   │
   ▼
Groq AI API
   │
   ▼
Generated Blog
   │
   ├── Display on Screen
   ├── Save to File
   └── Store in History
```

---

# 📦 Dependencies

- Flask
- Groq
- python-dotenv
- gunicorn
- markdown
- reportlab
- python-docx

---

# 🎯 Project Objectives

- Develop an AI-powered blog generation platform.
- Integrate Large Language Models using the Groq API.
- Generate SEO-friendly and structured blog articles.
- Learn Flask backend development.
- Understand REST API integration.
- Practice prompt engineering.
- Deploy a production-ready web application.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Python Programming
- Flask Framework
- REST API Integration
- Groq AI API
- Prompt Engineering
- Environment Variable Management
- Frontend & Backend Integration
- Error Handling & Logging
- File Management
- Responsive UI Design
- Render Deployment
- Git & GitHub Version Control

---

# 🚀 Future Enhancements

- User Authentication
- PDF Export
- DOCX Export
- AI Image Generation
- Multi-language Support
- Blog Categories
- Rich Text Editor
- Grammar Checker
- AI Rewrite Feature
- Word Counter
- Dark Mode
- Cloud Database Integration
- User Dashboard

---

# 👨‍💻 Author

**Amritanshu Shukla**

Final Year B.Tech (Computer Science Engineering - IoT)

### Connect with Me

**GitHub**  
https://github.com/amritanshu1968-wq

**LinkedIn**  
https://www.linkedin.com/in/amritanshu-shukla-2253203a3

---

# 🙏 Acknowledgements

- Groq AI
- Flask Community
- Render
- Python Community
- Open Source Contributors

---
This project was developed as part of my **Internship & Training Program** for educational and learning purposes.

© 2026 Amritanshu Shukla. All Rights Reserved.
