from datetime import timedelta
import os
from sensor.constant import training_pipeline
from sensor.constant.training_pipeline import ARTIFACT_DIR, PIPELINE_NAME
from datetime import datetime

class TrainingPipelineConfig:
    def __init__(self,timestamp:datetime=datetime.now()):
        timestamp_str = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        self.pipeline_name = PIPELINE_NAME
        self.artifact_dir = os.path.join(ARTIFACT_DIR,timestamp_str)
        self.timestamp = timestamp
        self.time_to_live = timedelta(days=30)

class data_ingestion_config:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
        self.ingested_dir = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR)
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME