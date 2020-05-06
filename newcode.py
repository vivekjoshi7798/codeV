import time
def gen(num):
    l=[]
    for i in range(num):
        l.append(i)
    return l
        
def genrator(num):
    for i in range(num):
        yield i

t1=time.clock()
f=genrator(1000)
t2=time.clock()
print("Time : ",t2-t1)

t1=time.clock()
l=gen(1000)
t2=time.clock()
print("Time for list: ",t2-t1)
