
'''printing Extram daat '''
import module1 as m1
import os

print (m1.add(10,20))
print(dir(m1))
print('Module : ',m1.__name__)
print('Module : ',m1.__doc__)
print('Module : ',m1.__file__)

print(os.path.dirname(__file__))


print("for main FILE : ",__name__)
print("for main FILE : ",__doc__)
print("for main FILE : ",__file__)