def is_prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime")
x=int(input("enter the number: "))
is_prime(x)
