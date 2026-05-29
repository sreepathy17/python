def prime(x):
    y=0
    for i in range(1,x+1):
        if x%i==0:
            y+=1 
    if y==2:
        print("prime")
    else:
        print("not prime")           
prime(17) 
prime(12)       
