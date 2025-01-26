import logging

def setup_logger():
    """Setup the logger for the application."""
    logger = logging.getLogger("memorylane")
    logger.setLevel(logging.DEBUG)  # Set default log level to INFO

    # Create a console handler for logging to the terminal
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # Set console log level to INFO

    # Create a formatter for log messages
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger

logger = setup_logger()