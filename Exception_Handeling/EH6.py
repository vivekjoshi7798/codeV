#nestedtryexceptblock

try :
    print(10/0)
    try :   
            x=int(input("Enter a value"))
            y=int(input("Enter a value"))
            print(x/y)
    except  ValueError:
            print("INNER EXCEPTION HANDELING value Error")
    finally : 
            print("INNER FINALLY Program excecutted successfully") 
except (ZeroDivisionError,ValueError) as E :
    print("OUTER EXCEPTION HANDELING Exception is :  ",E.__class__.__name__)

finally : 
        print("OUTER FINALLY Program excecutted successfully")    