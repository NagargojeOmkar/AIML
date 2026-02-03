from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

class TrainingPipeline:
    def run(self):
        train_path, test_path = DataIngestion().run()

        DataValidation().run(train_path)

        X_train, y_train, X_test, y_test = DataTransformation().run(train_path, test_path)

        model = ModelTrainer().run(X_train, y_train)

        acc = ModelEvaluation().run(model, X_test, y_test)
        print("Test Accuracy:", acc)
