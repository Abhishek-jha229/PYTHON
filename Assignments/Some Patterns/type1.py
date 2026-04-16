"""
Program: Number Pattern Printer
-------------------------------
This program prints a simple number pattern based on user input.

Pattern Example (for input = 5):
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

# Taking input from user
x = int(input("enter the number: "))

def row(a):
    """
    Function to print a number pattern.

    Parameters:
    a (int): Number of rows for the pattern

    Returns:
    None
    """
    # Loop through each row
    for i in range(1, a + 1):
        # Print numbers from 1 to current row number
        for j in range(1, i + 1):
            print(j, end=" ")
        # Move to next line after each row
        print()

# Calling the function
row(x)
