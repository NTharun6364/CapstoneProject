# import logging
# import os
# from datetime import datetime


# def setup_logger():
#     # Determine project root and logs directory
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     logs_dir = os.path.join(base_dir, 'logs')
#     if not os.path.exists(logs_dir):
#         os.makedirs(logs_dir)

#     # Use a stable log filename so all runs append to the same file
#     log_file = os.path.join(logs_dir, 'parabank.log')

#     # Create a logger
#     logger = logging.getLogger('parabank_automation')
#     logger.setLevel(logging.INFO)

#     # Clear existing handlers to avoid duplicate logging if module re-imported
#     if logger.hasHandlers():
#         logger.handlers.clear()

#     # Create file handler with append mode and UTF-8 encoding
#     file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')

#     # Create detailed formatter (include filename and line number)
#     detailed_format = logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
#     )
#     file_handler.setFormatter(detailed_format)

#     # Add the file handler
#     logger.addHandler(file_handler)

#     # Prevent propagation to the root logger (avoids double output under some runners)
#     logger.propagate = False

#     # Expose the logfile path for diagnostics
#     logger.logfile = log_file

#     return logger


# # Create a global logger instance
# logger = setup_logger()


# if __name__ == '__main__':
#     print('Logging to', logger.logfile)

import logging
import os
from datetime import datetime

def setup_logger(test_name=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_dir = os.path.join(base_dir, 'logs')
    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = test_name or "test"
    log_file = os.path.join(logs_dir, f"{name}_{timestamp}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()

    fh = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(sh)

    logger.propagate = False
    logger.logfile = log_file
    return logger

# Optional global logger
logger = setup_logger("global")

if __name__ == '__main__':
    print('Logging to', logger.logfile)
