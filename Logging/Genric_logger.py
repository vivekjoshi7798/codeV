import logging
import inspect

def createLogger(level):
    function_name= inspect.stack()[1][3]
    logger =logging.getLogger(function_name)
    logger.setLevel(level)
    handeller=logging.FileHandler('Logging/{}.log'.format(function_name),mode='w')
    FMTR=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt='%A %B %d/%m/%y-%I:%M:%S %p')
    handeller.setFormatter(FMTR)
    logger.addHandler(handeller)
    logger.critical("critical error system was Down")
    logger.error("error system was Down")
    logger.warning(" warning error system was Down")
    logger.info("  info system was Down")
    logger.debug(" debug error system was Down")
    return logger