# class person:
#     def person(self,name,age):
#         print(name,age)
# class student(person):
#     def student(self,grade):
#         print(grade)        
# s=student()
# s.person("pathy",16)
# # s.student(11)       


# class animal:
#     def eat(self):
#         print("animal eats")
# class dog(animal)
#     def bark(self):
#         print("dog barks")
# d=dog()
# # d.eat()
# # d.bark()


# class employee:
#     def employee(self,name,salary):
#         print(name,salary)
# class manager(employee):
#     def manager(self,department):
#         print(department)
# m=manager()
# m.employee("govind",50000)
# m.manager("GND")


# class grandparent:
#     def grandparent(self):
#         print("grandparent")
# class parent(grandparent):
#     def parent(self):
#         print("parent")
# class child(parent):
#     def child(self):
#         print("child")
# c=child()
# c.grandparent()
# c.parent()
# c.child()                       


class person:
    def __init__(self,name):
        self.name=name
class teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def display(self):
        print(self.name,self.subject)
t=teacher("govind","boxing")   
t.display()
                   