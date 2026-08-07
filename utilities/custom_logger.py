import logging
import os
from datetime import datetime

class LogMaker:
    @staticmethod
    def log_gen(logger_name="HybridFramework"):

        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger(logger_name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            log_file = os.path.join(
                "logs",
                f"HybridFramework_{datetime.now().strftime('%Y%m%d')}.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )

            # File Handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger






