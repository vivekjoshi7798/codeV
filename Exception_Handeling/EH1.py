try:
    print(10/0)

except ZeroDivisionError as E:
    print('not poswilr to excecutre ',E.__class__.__name__)
    print('not poswilr to excecutre ',type(E))
    print('not poswilr to excecutre ',E)