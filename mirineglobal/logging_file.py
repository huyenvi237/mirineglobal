import  logging

logger = logging.getLogger('Output_logging_file')
file_logger = logging.FileHandler('ouput_logging_file.log')
new_format = '[%(asctime)s] - [%(levelname)s] - %(message)s'
file_logger_format = logging.Formatter(new_format)

file_logger.setFormatter(file_logger_format)
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('Output_logging_file').addHandler(console)
logger.info('info')
logger.warning('warning')
logger.error('error')
