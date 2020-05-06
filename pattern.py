#print the patert

n=int(input("ROWS : "))
i=1
j=0
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ') 
    print()

# OUTPUT
# ROWS : 4
# * 
# * * 
# * * * 
# * * * *     



# n=int(input("ROWS : "))
# i=1
# j=0
# for i in range(1,n+1):
#         print("*"*i) 