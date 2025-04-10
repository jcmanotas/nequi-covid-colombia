import logging
import os
from datetime import datetime

def get_logger(name: str) -> logging.Logger:
    logs_dir = os.path.join("logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
    log_path = os.path.join(logs_dir, log_filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitar agregar múltiples handlers al mismo logger
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
