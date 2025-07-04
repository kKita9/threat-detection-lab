import logging
from logging.handlers import RotatingFileHandler
import os
import json

def setup_logger(name, log_folder, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', log_folder, log_file)

    if not logger.handlers:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

        file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def jsonl_result(result, log_folder, log_file):
    log_file = os.path.join(os.path.dirname(__file__), '..', 'logs', log_folder, log_file)

    with open(log_file, 'a') as f:
        f.write(json.dumps(result) + '\n')