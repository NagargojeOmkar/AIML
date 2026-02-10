from dataclasses import dataclass
import os
import pymongo
from dotenv import load_dotenv

@dataclass
class DataIngestionConfig:
    raw_data_path: str = "artifacts/raw.csv"
    train_path: str = "artifacts/train.csv"
    test_path: str = "artifacts/test.csv"

@dataclass

class env_variable:
    mongodb_uri: str = os.getenv("mongodb_uri") 

env_var = env_variable()

mongodb_client = pymongo.MongoClient(env_var.mongodb_uri)


