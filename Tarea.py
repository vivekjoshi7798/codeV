a=float(input("Enter a 1st side :"))
b=float(input("Enter a 1st side :"))
c=float(input("Enter a 1st side :"))

S=(a+b+c)/2

area=(S*(S-a)*(S-b)*(S-c))**0.5

print("Area : ",area)
