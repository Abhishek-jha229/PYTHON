# Reverse Right-Angled Number Pattern in Python

# A simple Python program to print a reverse right-angled number pattern using nested loops and spaces.

x=int(input("Enter the number: "))

def row(a):

    # Outer loop for rows
    for i in range (1,a+1):

        # Printing leading spaces
        print("  "*(i-1),end="")

        # Printing numbers
        for j in range(i,a+1):
            print(j,end=" ")

        # Moving to next line
        print()

# Calling the function
row(x)
