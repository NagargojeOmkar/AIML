import os

# =========================
# BASIC PROJECT CONSTANTS
# =========================

TARGET_COLUMN: str = "class"

PIPELINE_NAME: str = "sensor_fault_detection"
ARTIFACT_DIR: str = os.path.join("artifacts", PIPELINE_NAME)

FILE_NAME: str = "sensor.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# =========================
# PREPROCESSING / MODEL FILES
# =========================

PREPROCESSOR_OBJECT_FILE_NAME: str = "preprocessor.pkl"
MODEL_FILE_NAME: str = "model.pkl"

# =========================
# SCHEMA
# =========================

SCHEMA_FILE_PATH: str = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS: str = "drop_columns"

# =========================
# DATA INGESTION CONSTANTS
# =========================

DATA_INGESTION_COLLECTION_NAME: str = "training_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
