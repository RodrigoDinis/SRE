import logging
from logging.handlers import RotatingFileHandler

#    Notes
#    logger.debug("This is a debug message")
#    logger.info("This is an info message")
#    logger.warning("This is a warning message")
#    logger.error("This is an error message")
#    logger.critical("This is a critical message")



def setup_logger():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the log level
    file_handler = RotatingFileHandler("../logs/get_weather.log", maxBytes=1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)


    # Create a console handler and set the log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set the format for the log records
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

