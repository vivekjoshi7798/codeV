import logging
#create logger
logger=logging.getLogger('demo1')
#set level
logger.setLevel(logging.DEBUG)
#create handeler file,stream or SMTP
ConHand1= logging.StreamHandler()
ConHand2= logging.FileHandler('Logging/abc.log',mode='a');
#handeler is responcile for level
ConHand1.setLevel(logging.ERROR)
ConHand2.setLevel(logging.DEBUG)


#create formatter

formater=logging.Formatter('%(levelname)s:%(message)s')
formater2=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt='%A %B %d/%m/%y-%I:%M:%S %p')

# aatach formater to handeler
ConHand1.setFormatter(formater)
ConHand2.setFormatter(formater2)

# aatach handeler to logger
logger.addHandler(ConHand1)
logger.addHandler(ConHand2)

logger.critical("critical error system was Down")
logger.error("error system was Down")
logger.warning(" warning error system was Down")
logger.info("  info system was Down")
logger.debug(" debug error system was Down")
