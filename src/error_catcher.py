import logging

def catch_error(error_message):
    logger = logging.getLogger(__name__)
    logger.error(error_message)
