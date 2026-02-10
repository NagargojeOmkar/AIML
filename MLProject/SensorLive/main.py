from sensor.logger import logging
from sensor.exception import CustomException
from sensor.pipelines.training_pipeline import TrainingPipeline
from sensor.utils import dump_csv_file_to_mongodb  
from sensor.config import env_var, mongodb_client


import sys


def main():
    try:
        logging.info("==== ML Pipeline Execution Started ====")

        pipeline = TrainingPipeline()
        pipeline.run()

        logging.info("==== ML Pipeline Execution Completed ====")

    except Exception as e:
        logging.error("Pipeline execution failed")
        raise CustomException(e, sys)


if __name__ == "__main__":
    file_path = r"C:\Users\Imnag\Desktop\DSML\MLProject\SensorLive\aps_failure_training_set.csv"
    database_name = "SensorLive"
    collection_name = "training_data"


if mongodb_client[database_name][collection_name].count_documents({}) == 0:
    dump_csv_file_to_mongodb(file_path, database_name, collection_name)

    main()
