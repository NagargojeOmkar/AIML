import pandas as pd
from src.exception import CustomException

class DataValidation:
    def run(self, train_path):
        try:
            df = pd.read_csv(train_path)

            if df.isnull().sum().sum() > 0:
                raise Exception("Missing values found")

            return True
        except Exception as e:
            raise CustomException(e)
