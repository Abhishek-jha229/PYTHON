# Hollow Rectangle Pattern in Python

# A simple Python program to print a hollow rectangle star pattern using nested loops and conditional statements.

rows=int(input("enter rows: "))
cols=int(input("enter cols: "))

def pattern(a,b):

    # Outer loop for rows
    for i in range(rows):

        # Inner loop for columns
        for j in range(cols):

            # Checking border positions
            if i==0 or i==rows-1 or j==0 or j==cols-1:
                print("*",end=" ")

            # Printing spaces inside rectangle
            else:
                print(" ",end=" ")

        # Moving to next line
        print()

# Callin the function
pattern(rows,cols)
