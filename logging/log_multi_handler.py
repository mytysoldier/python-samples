from logging import getLogger, FileHandler, Formatter, DEBUG, ERROR

formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)

handler = FileHandler('log2.txt')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

error_handler = FileHandler('error.txt')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(error_handler)

logger.info('program started')
logger.debug('input is 1000')
logger.warning('file exceeded')
logger.error('file not exist')