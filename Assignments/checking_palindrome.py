x=int(input("enter the number: "))
def palindrome(a):
    original=a
    reverse=0
    while a>0:
        digit = a%10
        reverse=reverse*10 + digit
        a=a//10
    return original==reverse
print(palindrome(x))
        
