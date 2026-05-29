class car:
    def stop(self):
        print("stop")
class bike:
    def stop(self):
        print("start")
c=car()
b=bike()
c.stop()
b.stop()

class teacher:
    def work(self):
        print("stop talking")
class student:
    def work(self):
        print("ok miss") 
t=teacher()
s=student()
t.work()
s.work()


class bird:
    def fly(self):
        print("bird is flying")
class airplane:
    def fly(self):
        print("airplane is on the wayon air") 
b=bird()
a=airplane()
b.fly()
a.fly()


class email:
    def message(self):
        print("email receives")
class sms:
    def message(self):
        print("sms receives") 
e=email()
s=sms()
e.message()
s.message()