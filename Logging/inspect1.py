import inspect 

def getInfo():
    print(inspect.stack()[1][3])