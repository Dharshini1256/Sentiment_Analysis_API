**Sentiment Analysis REST API**
**Project Overview**
This project is a RESTful API built using FastAPI that performs real-time sentiment analysis on text input.

**It supports:**
-Single text prediction
-Batch sentiment prediction
-Health check endpoint

**Tech Stack**
-Python
-FastAPI
-TextBlob
-Uvicorn

**API Endpoints**
GET /health
Returns API health status.
POST /predict
Predict sentiment for single text.

**Example Input:**

{
  "text": "I love AI"
}

POST /batch-predict

Predict sentiment for multiple texts.

**Example Input:**

{
  "texts": [
    "I love this",
    "This is bad"
  ]
}

**How to Run**
Create virtual environment

**Install dependencies:**
pip install -r requirements.txt

**Run server:**
uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs


