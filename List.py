row=int(input("Enter  A number of Rows"))
col=int(input("Enter  A number of Col"))
matrix=[]

for i in range(0,row):    
    Trow=[]
    for j in range(0,col):
        k=int(input("enter value for position [{}][{}] :".format(i,j)))
        Trow.append(k)
    
    matrix.append(Trow)
print(matrix)    