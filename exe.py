try:
    num=int(input("enterthe number:"))
    print(10/num)
except ZeroDivisionError:
    print("error")
else:
    print("division sucessfully")
finally:
    print("program ended")

