# 🧠 AI Diagnosis Model API – Backend

This is the backend service for the medical diagnosis app. It serves a trained AI model through RESTful API endpoints. The service receives patient data (e.g. images), performs inference using the AI model, and returns diagnostic results.
     
---

## 🚀 Features

- 🧬 AI model for disease diagnosis
- 📤 Accepts image upload via HTTP
- 📊 Returns prediction results in JSON
- 🔐 CORS enabled for frontend/mobile integration
- 📂 Easily extendable for new models or endpoints

---

## 🏗️ Tech Stack

- Python 3.10+
- Flask 
- Uvicorn (for ASGI serving)
- TensorFlow 
- CORS middleware
- Pydantic for input validation

---

## 📦 Project Structure

