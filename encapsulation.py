# class bank:
#     def __init__(self):
#         self.__balance=1000#private
#     def deposit(self,amount):
#         self.__balance+=amount
#     def get__balance(self):
#         return self.__balance
#     def withdraw(self,amount):
#         self.__balance-=amount
# b=bank()
# b.deposit(500)
# print(b.get__balance()) 
# b.withdraw(1000)    
# print(b.get__balance())

# class student:
#     def __initi__(self):
#         self.__marks=80#private
#     def set_marks(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         print(self.__marks)
# m=student()
# m.set_marks(70)
# m.get_marks()   

# class employee:
#     def __init__(self):
#         self.__salary=15000
#     def  upgrade_salary(self,increment):
#         self.__salary+=increment
#     def display(self):
#         print(self.__salary) 
# e=employee()
# e.upgrade_salary(5000)
# e.display()

# class user:
#     def __init__(self):
#         self.__password=2255
#     def  set_password(self,password):
#         self.__password=password
#     def validate_password(self,password):
#         if self.__password==password:
#             print("corect password")
#         else:
#             print("wrong password")
# u=user()
# u.set_password(789456123)
# u.validate_password(789456123)

class product:
    def __int__(self):
        self.__price=299
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        print(self.__price)
p=product()
p.set_price(299)
p.get_price()               