try:
    pin=(input("enter the password"))
    if len(pin)!=6:
        raise Exception("weak password")
    print("valid")
except:
    print("weak password")