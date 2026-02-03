import logging, os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=os.path.join("logs", LOG_FILE),
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
