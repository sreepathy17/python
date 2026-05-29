try:
    marks=float(input("enter your marks"))
    if marks<0 or marks>100:
        raise Exception("invalid marks")
    print("valid marks")
except:
    print("invalid marks")    