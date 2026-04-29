import logging
from datetime import datetime

class LogMaker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename='./logs/rahulshettyacademy.log',
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%Y-m-%d %H:%M:%S %p', force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


