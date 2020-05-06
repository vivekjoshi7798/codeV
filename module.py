import time
import clock as c
from clock import add as addition
from clock import m as D
from importlib import reload

print(c.add(10,20))
time.sleep(10)
reload(c)
print(c.add(10,20))


print(c.mul(10,20))
print(c.sub(10,20))
print(c.div(10,20))
print(c.div(10,0))
print("number ",c.m," ",D,end='')
print(addition(50,60))
