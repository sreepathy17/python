
class phone:
    def __init__(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def display(self):
        print(self.brand,self.ram,self.storage)

        
p=phone("oppo","4GB","68GB")
p.display()
     