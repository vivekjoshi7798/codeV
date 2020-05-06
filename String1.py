#string 

s1=input("Enter a string : ")
i=0
print("CHAR \tpos \tneg")
for x in s1:
    print(x,'\t',i,'\t',i-len(s1))
    i+=1
