# 🏥 Explainable AI Disease Prediction System

## 📌 Overview

This project is a Machine Learning-based disease prediction system that analyzes user symptoms and predicts possible diseases. It also provides explanations and chatbot-based health suggestions.

---

## 🎯 Features

* 🧠 Disease prediction using ML
* 🔍 Explainable AI output
* 💬 Chatbot assistance
* 🌐 REST API using Flask
* 🐳 Docker containerization

---

## 🌍 SDG Alignment

This project supports **UN SDG 3: Good Health and Well-being**, promoting accessible healthcare guidance.

---

## 🛠 Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* Docker

---

## ⚙️ How to Run

### ▶️ Option 1 — Run Locally

```bash
pip install -r requirements.txt
python model.py
python app.py
```

---

### 🐳 Option 2 — Run with Docker

```bash
docker build -t disease-ai .
docker run -p 5000:5000 disease-ai
```

---

## 🔌 API Usage

### Endpoint:

```
POST /predict
```

### Request:

```json
{
  "fever": 1,
  "cough": 1,
  "fatigue": 1
}
```

---

## 📊 Example Output

```json
{
  "disease": "Flu",
  "explanation": "Prediction based on symptoms",
  "chatbot": "Flu is a viral infection. Rest and hydrate."
}
```

---

## 🧩 Project Structure

```
.
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚠️ Limitations

* Small dataset
* Not a substitute for professional medical advice

---

## 🚀 Future Improvements

* Larger medical datasets
* Integration with advanced AI models
* Deployment using Kubernetes

---

## 👩‍💻 Author

Sandiya
