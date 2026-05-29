
x=7
num=0
while num!=x:
    num=int(input("guess the number:"))    
    if num>x:
        print("Too High")
    elif num==x:
        print("corect")
    else:
        print("Too low")       