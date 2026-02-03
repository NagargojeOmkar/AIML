import joblib, pandas as pd

class PredictionPipeline:
    def predict(self, input_dict):
        model = joblib.load("artifacts/model.pkl")
        pre = joblib.load("artifacts/preprocessor.pkl")

        df = pd.DataFrame([input_dict])
        X = pre.transform(df)
        return model.predict(X)[0]
