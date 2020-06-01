
try :
    x=int(input("Enter a value"))
    y=int(input("Enter a value"))
    print(x/y)
except BaseException as E :
    print("Exception is :  ",E.__class__.__name__)
    print("Exception is :  ",E)
    print("Exception is :  ",E)