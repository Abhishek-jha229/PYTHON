# Reverse Number Triangle Pattern in Python

# A simple Python program to print a reverse number triangle pattern using nested loops.

x = int(input("enter the number: "))

def row(a):
    for i in range (1,x+1):

        # Printing numbers in reverse order
        for j in range(x+1-i,0,-1):
            print(j,end=" ")

        # Moving to next line
        print()

# Calling the function
row(x)
