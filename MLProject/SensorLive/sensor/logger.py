import logging
import os
from datetime import datetime


# 🔹 Log folder create
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 🔹 Unique log file name with timestamp
LOG_FILE = datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)


# 🔹 Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(name)s — %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),   # file me save
        logging.StreamHandler()          # console me show
    ]
)

# 🔹 Logger object (optional — but useful)
logger = logging.getLogger("SensorLive")



"""

from sensor.logger import logger

logger.info("Data ingestion started")
logger.info("Model training completed")
logger.warning("Missing values detected")
logger.error("Training failed")

"""

