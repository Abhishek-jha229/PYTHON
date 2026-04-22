print("Armstrong numbers between 1 and 1000 are: ")
for num in range(1,1001):
    original=num
    sum_of_cubes=0
    temp=num
    while temp>0:
        digit=temp%10
        sum_of_cubes+=digit**3
        temp=temp//10
    if original==sum_of_cubes:
        print(original)
