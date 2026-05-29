
x=int(input("enter the number="))
y=int(input("enter the second number="))
z=int(input("enter the third number="))
if x>y>z:
    print ("x is greater")
elif y>x>z or y>z>x:
    print ("y is greater") 
else:
    print ("z is grater")       