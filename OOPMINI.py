class bank:
    """HI I am BANK APPLICATION"""
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    
    def diposite(self,amount):
        self.balance=self.balance+amount
        print("Reamaining_amount : ",self.balance)
        
    def widraw(self,amount):
        if amount>self.balance:
            print("Insufficiant Balance")
        else:
            self.balance=self.balance-amount
            print("diposited amount is: ",amount,"Reamaining_amount : ",self.balance)
       
k=int(input("Enter A number OF student"))            

for i in range(k):
    name=input("Enter A Name : ")
    B=bank(name)
    while True:
        option=int(input("\n Enter Option \n 1.DIP \n 2.Widrwal \n 0-Exit\n"))
     
        if option==0: 
            break
        elif option==1:
            amount=int(input("Enter A amount to diposite")) 
            B.diposite(amount)
        elif option==2:
            amount=int(input("Enter A amount to diposite"))
            B.widraw(amount)
        else:
            print("wrong Input selection")
        