import logging
#create logger
logger=logging.getLogger('Student')
#set level
logger.setLevel(logging.DEBUG)
#create handeler file,stream or SMTP
ConHand= logging.FileHandler('Logging/abc.log',mode='a');
#handeler is responcile for level
ConHand.setLevel(logging.ERROR)
#create formatter
formater=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt='%A %B %d/%m/%y-%I:%M:%S %p')
# aatach formater to handeler
ConHand.setFormatter(formater)
# aatach handeler to logger
logger.addHandler(ConHand)
logger.critical("critical error system was Down")
logger.error("error system was Down")
logger.warning(" warning error system was Down")
logger.info("  info system was Down")
logger.debug(" debug error system was Down")
