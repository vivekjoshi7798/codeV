import logging

logging.basicConfig(filemode='a',filename='Logging/L3.log',format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%A %B %d/%m/%y-%I:%M:%S %p',level=10)



try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    d=a/b
    logging.critical("DIVISION IS {0}".format(d))
except ZeroDivisionError as msg:
    logging.exception(msg)
except ValueError as msg:
    logging.exception(msg)
else:
    logging.critical('********************CODE EXECUTION SUCESSFUL**********************\n\n')
