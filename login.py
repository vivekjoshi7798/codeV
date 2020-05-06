print('facebook.com')

USERNAME=input("USERNAME\t")
PASSWORD=input("PASSWORD\t")

while ((USERNAME!='admin') or (PASSWORD!='admin')):
    print('authentication error\n Please Enter details again',)
    USERNAME=input()
    PASSWORD=input()
    
print(' login Successful')  