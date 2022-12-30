from logging import getLogger, FileHandler, Formatter, DEBUG

formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)
handler = FileHandler('log.txt')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)

logger.debug('input is 1000')
logger.error('file not exist')