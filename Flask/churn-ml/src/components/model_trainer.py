from sklearn.ensemble import RandomForestClassifier
import joblib

class ModelTrainer:
    def run(self, X, y):
        model = RandomForestClassifier()
        model.fit(X, y)

        joblib.dump(model, "artifacts/model.pkl")
        return model
