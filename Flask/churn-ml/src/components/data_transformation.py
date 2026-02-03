import pandas as pd
import joblib

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


class DataTransformation:
    def run(self, train_path, test_path):
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        X_train = train_df.drop("Churn", axis=1)
        y_train = train_df["Churn"]

        X_test = test_df.drop("Churn", axis=1)
        y_test = test_df["Churn"]

        num_cols = X_train.select_dtypes(exclude="object").columns
        cat_cols = X_train.select_dtypes(include="object").columns

        preprocessor = ColumnTransformer([
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(), cat_cols)
        ])

        X_train_trans = preprocessor.fit_transform(X_train)
        X_test_trans = preprocessor.transform(X_test)

        joblib.dump(preprocessor, "artifacts/preprocessor.pkl")

        return X_train_trans, y_train, X_test_trans, y_test
