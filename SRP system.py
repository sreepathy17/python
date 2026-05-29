total = 0
x = 0
fail = 0
for i in range(1,6):
    mark = int(input("enter marks:"))
    total += mark

    if mark > 24:
        x += 1
        print("pass")
    elif mark < 24:
        fail += 1
        print("fail")
    else:
        print("invalid")   

average = total/500*100
print(average)
print(x)
print(fail)             