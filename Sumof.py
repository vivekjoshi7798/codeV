
#Smart Validation
def Pylang(funct):
  def inner(a,b): 
    if b==0:
        print("cannot Devide by zero")
    else : 
        return funct(a,b)
  return inner
@Pylang
def lang(a,b):
     print("Division is",a/b)

lang(10,0)
lang(20,3)
lang(130,0)