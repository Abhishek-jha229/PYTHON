# Pyramid Star Pattern in Python

A simple Python program to print a centered pyramid star (`*`) pattern using nested loops and spaces.

x =int(input("enter the number: "))

def pattern(a):

    # Outer loop for rows
    for i in range(1,a+1):

        # Printing leading spaces
        print("  "*(a-i),end="")

        # Printing stars
        for j in range(1,(2*i)):
            print("*",end=" ")

        # Moving to next line
        print()
# Calling the function
pattern(x)
