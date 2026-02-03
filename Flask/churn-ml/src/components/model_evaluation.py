from sklearn.metrics import accuracy_score

class ModelEvaluation:
    def run(self, model, X, y):
        preds = model.predict(X)
        acc = accuracy_score(y, preds)
        return acc
