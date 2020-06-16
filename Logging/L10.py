from  Genric_logger import createLogger
import logging

def f1():
   logger=createLogger(logging.DEBUG)
   logger.info('EXECUTION STOP')

def f2():
   logger=createLogger(logging.WARNING)



def f3():
   logger=createLogger(logging.ERROR)   

f1()
f2()
f3()


