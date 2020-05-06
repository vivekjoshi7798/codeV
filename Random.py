import random
list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
city=['Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata']
des=['Trainee Engineer','Software Engineer','System Analyst','Programmer Analyst Engineer','Senior Software','Project Lead','Project Manager','Program Manager']

for i in range(15):

    print("Employee NAME : ",random.choice(list),end='',sep='')
    for i in range(random.randrange(2,6)):
        print(random.choice(list).lower(),end='',sep='')

    print("\nEmployee ID   : e-",random.randint(0,9) ,end='',sep='')
    for i in range(4):
            print(random.randint(0,9),end='',sep='')

    print("\nEmployee city : ",random.choice(city),end='',sep='')

    print("\nEmployee Salarie : ",random.randrange(100000,500000),end='',sep='')

    print("\nMobile Number : ",random.randrange(6,9),end='',sep='')
    for i in range(9):
        print(random.randint(0,9),end='',sep='')

    print("\nEmployee desiganation : ",random.choice(des),end='',sep='')

    print("\n**********************************************************")
