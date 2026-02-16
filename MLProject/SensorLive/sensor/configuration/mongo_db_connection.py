from dotenv import load_dotenv
import os
from sensor.constant import training_pipeline
import certifi

ca = certifi.where()
import pymongo
from sensor.constant.database import DATABASE_NAME

from sensor.constant.env_variable import MONGODB_URL_KEY, MONGODB_NAME_KEY

import os
import logging

load_dotenv()


class MongoDBClient:
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Connecting to MongoDB at {mongo_db_url}")

                if localhost in mongo_db_url:
                    logging.warning(
                        "Connecting to MongoDB at localhost. Ensure MongoDB is running locally."
                    )
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(
                        mongo_db_url, tlsCAFile=ca
                    )

                logging.info("Successfully connected to MongoDB.")

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Using MongoDB database: {database_name}")

        except Exception as e:
            logging.error(f"Error connecting to MongoDB: {e}")
            raise e
