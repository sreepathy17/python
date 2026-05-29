class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(self.brand,self.model,self.price)

        
c=car("ertiga","2021-zxi",1375000)
c.display()
     