from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    analysis = TextBlob(input.text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "input_text": input.text,
        "sentiment": sentiment,
        "confidence": round(abs(polarity), 2)
    }
@app.get("/health")
def health_check():
    return {"status": "API is running properly"}
from typing import List

class BatchTextInput(BaseModel):
    texts: List[str]
@app.post("/batch-predict")
def batch_predict(input: BatchTextInput):
    results = []

    for text in input.texts:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        results.append({
            "text": text,
            "sentiment": sentiment,
            "confidence": round(abs(polarity), 2)
        })

    return {"results": results}

