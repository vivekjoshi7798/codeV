Num=int(input("enter a number"))
i=0
flag=0
COND=int(Num/2)
for i in range (2,COND):
      if Num%i==0:
        flag=1

if flag==0:
    print("NUM {} is prime".format(Num))
else:
    print("NUM {} is NOT prime".format(Num))


#     enter a number18
# NUM 18 is NOT prime
# PS C:\VPYTHON>
