import logging 
logging.basicConfig(filename='Log.txt',level=logging.DEBUG)
logging.critical("critical error system was Down")
logging.error("error system was Down")
logging.warning(" warning error system was Down")
logging.info("  info system was Down")
logging.debug(" debug error system was Down")
log = logging.getLogger("my-logger")
print(log,__name__)