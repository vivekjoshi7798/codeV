try :
    x=int(input("Enter a value"))
    y=int(input("Enter a value"))
    print(x/y)
except (ZeroDivisionError,ValueError) as E :
    print("Exception is :  ",E.__class__.__name__)
    