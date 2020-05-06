class Student: 

    def __init__(self,Name,Mark):
        self.name=Name
        self.mark=Mark

    def disp(self):
        print(self.name)        
        print(self.mark)

    def grade(self):
        if self.mark>75 :
            print("mark is greater than 75 dist")
        elif self.mark<75 and self.mark>60 :     
            print("first class")    
        elif self.mark<60 and self.mark>35 :     
            print("second class")
        else:     
            print("Failed")

for i in range(5):
    print("enter name and mark of student")
    name=input("enter name")
    mark=int(input("enter mark"))
    S=Student(name,mark)
    S.disp()
    S.grade()

    