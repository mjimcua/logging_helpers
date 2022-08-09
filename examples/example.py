from logging_helpers.LoggerManager import LoggerManager

if __name__ == "__main__":

    logger = LoggerManager('DEBUG').get_logger_configured()

    logger.debug('Debug log')
    logger.info('Info log')
    logger.warning('Warning log')
    logger.error('Error log')
