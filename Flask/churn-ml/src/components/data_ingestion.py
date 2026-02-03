import pandas as pd, os
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException

class DataIngestion:
    def run(self):
        try:
            logging.info("Ingestion started")

            df = pd.read_csv("data/churn.xls")

            os.makedirs("artifacts", exist_ok=True)
            df.to_csv("artifacts/raw.csv", index=False)

            train, test = train_test_split(df, test_size=0.2, random_state=42)
            train.to_csv("artifacts/train.csv", index=False)
            test.to_csv("artifacts/test.csv", index=False)

            logging.info("Ingestion completed")
            return "artifacts/train.csv", "artifacts/test.csv"

        except Exception as e:
            raise CustomException(e)
