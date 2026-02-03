from flask import Flask, request, jsonify
from src.pipelines.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    pred = PredictionPipeline().predict(data)
    return jsonify({"churn": bool(pred)})

@app.route("/", methods=["GET"])
def home():
    return "Churn ML API is running"


app.run()
