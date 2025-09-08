# utils/logger.py

import logging
from logging.handlers import RotatingFileHandler

def get_logger(name: str = "gridiron"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Console handler
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter("[%(asctime)s] %(levelname)s — %(message)s", "%H:%M:%S")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

        # File handler with rotation
        file_handler = RotatingFileHandler("logs/gridiron.log", maxBytes=1_000_000, backupCount=5)
        file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s — %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
