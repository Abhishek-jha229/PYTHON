# Right-Aligned Hash Triangle Pattern in Python

# A simple Python program to print a right-aligned triangle pattern using the `#` symbol.

x=int(input("enter the number: "))

def pattern(a):

    # Outer loop for rows
    for i in range(1,a+1):

        # Printing leading spaces
        print("  "*(a-i),end="")

        # Printing hash symbols
        for j in range(1,i+1):
            print("#",end=" ")

        # Moving to next line
        print()
# Calling the function
pattern(x)
