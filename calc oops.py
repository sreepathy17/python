x=int(input("enter the first number"))
y=int(input("enter the second number"))
class calc:
    def add(self,x,y):
        print(x+y)
    def subtract(self,x,y):
        print(x-y)  
    def multiple(self,x,y):
        print(x*y)    
    def division(self,x,y):
        print(x/y)  
        
c=calc()
c.add(x,y)
c.subtract(x,y)
c.multiple(x,y)
c.division(x,y)