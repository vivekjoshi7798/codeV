n=len(s1)
i=n
i=i-1
while i!=-1:
    print (s1[i],end='')
    i -=1

#backword direction
n=len(s1)
i=-1
while i>=-n:
    print (s1[i],end='')
    i -=1
    


s=input("Enter main string:")
subs=input("Enter sub string:")
try:
n=s.index(subs)
except ValueError:
print("substring not found")
else:
print("substring found")   