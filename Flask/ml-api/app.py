from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/health", methods=["GET"])
def health():
    return {"status": "running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = [
        data["age"],
        data["salary"],
        data["experience"]
    ]

    prediction = model.predict([features])

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
