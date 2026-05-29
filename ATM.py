amount=int(input("enter the withdrawel amount: "))
balance=10000
if  balance<amount:
    print("insufficient amount")
elif amount%100==0:
    print("withdrawel successfuully")
    print("balance",balance-amount)
else:
    print("error")
