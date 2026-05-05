# Inverted Right Triangle Dollar Pattern in Python

# A simple Python program to print an inverted right triangle pattern using the `$` symbol.

x=int(input("enter the number: "))

def pattern(a):

    # Outer loop for rows
    for i in range(1,a+1):

        # Printing leading spaces
        print("  "*(i-1),end="")

        # Printing dollar symbols
        for j in range(i,a+1):
            print("$",end=" ")

        # Moving to next line
        print()

# Calling the function
pattern(x)
