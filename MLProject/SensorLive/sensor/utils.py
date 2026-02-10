import pandas as pd
import json
import logging
from sensor.config import mongodb_client


def dump_csv_file_to_mongodb(file_path: str, database_name: str, collection_name: str):
    try:
        logging.info("Reading CSV file")

        # read csv
        df = pd.read_csv(file_path)

        # reset index
        df.reset_index(drop=True, inplace=True)

        # dataframe → list of dict records
        records = json.loads(df.to_json(orient="records"))

        # get mongo collection
        collection = mongodb_client[database_name][collection_name]

        # insert
        collection.insert_many(records)

        logging.info(f"Inserted {len(records)} records into MongoDB")

    except Exception as e:
        logging.error(f"Mongo ingestion failed: {e}")
        raise e
