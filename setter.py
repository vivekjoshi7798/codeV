class Stud:

    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def setMark(self,mark):
        self.mark=mark
    
    def getMark(self):
        return self.mark
    
Student=[]
N=int(input("enter number of student You want to calculate"))

for i in range(N):
    S1=Stud()
    print("enter a name And Mark")
    Name=input("enter Name of Student")
    Mark=int(input("enter Mark of student"))
    S1.setName(Name)
    S1.setMark(Mark)
    Student.append(S1)
             
for i in Student:
    print(i.getName(),i.getMark())    


