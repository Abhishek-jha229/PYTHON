# Square Star Pattern in Python

# A simple Python program to print a square star (`*`) pattern using nested loops.


x=int(input("enter the number: "))

def row(a):

    # Outer loop for rows
    for i in range(1,x+1):

        # Inner loop for columns
        for j in range (1,x+1):
            print("*",end=" ")

        # Moving to next line
        print()

# Calling the function
row(x)
