# Repeated Number Triangle Pattern in Python

# A simple Python program to print a triangle pattern where each row contains repeated numbers equal to the row number.

x=int(input("enter the number: "))

def row(a):

    # Outer loop for rows
    for i in range(1,x+1):

        # Inner loop for printing numbers
        for j in range(i):
            print(i,end=" ")

        # Moving to next line
        print()

# Calling the function
row(x)
