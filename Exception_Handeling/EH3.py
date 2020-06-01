
try :
    x=int(input("Enter a value"))
    y=int(input("Enter a value"))
    print(x/y)
except ArithmeticError as AE:
    print("Exception is :  ",AE.__class__.__name__)
    print("aRTRMATIC eRROR")    
except ZeroDivisionError as E :
    print("Exception is :  ",E.__class__.__name__)
except ValueError as E1:
    print("Exception is :  ",E1.__class__.__name__)