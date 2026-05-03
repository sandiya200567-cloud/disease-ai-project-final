# 🏥 Explainable AI Disease Prediction System

## Overview
This project predicts diseases based on symptoms using Machine Learning and provides explanations with a chatbot.

## Features
- Disease prediction
- Explainable AI output
- Chatbot assistance
- Flask API
- Docker support

## How to Run

### Run Locally
pip install -r requirements.txt
python model.py
python app.py

### Run with Docker
docker build -t disease-ai .
docker run -p 5000:5000 disease-ai

## API Usage

POST /predict

{
  "fever": 1,
  "cough": 1,
  "fatigue": 1
}

## Example Output

{
  "disease": "Flu",
  "explanation": "Prediction based on symptoms",
  "chatbot": "Rest and hydrate"
}

## Author
Sandiya
