from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

def chatbot_response(disease):
    responses = {
        "Flu": "Flu is a viral infection. Rest and hydrate.",
        "Cold": "Common cold. Drink warm fluids and rest.",
        "Healthy": "You seem fine. Maintain a healthy lifestyle."
    }
    return responses.get(disease, "Consult a doctor.")

@app.route("/")
def home():
    return "Disease Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    fever = data["fever"]
    cough = data["cough"]
    fatigue = data["fatigue"]

    prediction = model.predict([[fever, cough, fatigue]])[0]

    explanation = f"Prediction based on fever={fever}, cough={cough}, fatigue={fatigue}"

    bot_reply = chatbot_response(prediction)

    return jsonify({
        "disease": prediction,
        "explanation": explanation,
        "chatbot": bot_reply
    })

if __name__ == "__main__":
    app.run(debug=True)