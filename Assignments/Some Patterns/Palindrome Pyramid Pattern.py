# Palindrome Pyramid Pattern in Python

# A simple Python program to print a palindrome number pyramid using nested loops.


x=int(input("enter the number: "))

def row(a):
    for i in range(1,5):

        # Printing spaces
        for j in range(x-i):
            print(" ",end=" ")

        # Printing numbers in reverse order
        for j in range(i,0,-1):
            print(j,end=" ")

        # Printing numbers in forward order
        for j in range(2,i+1):
            print(j,end=" ")

        # Moving to next line
        print()

# calling the function 
row(x)
