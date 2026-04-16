"""
Program: HCF (Highest Common Factor) Finder
-------------------------------------------
This program takes two integer inputs from the user
and calculates their HCF (Greatest Common Divisor)
using an iterative approach.

"""

# Taking input from user
x = int(input("enter a: "))
y = int(input("enter b: "))

# Finding minimum of the two numbers
z = min(x, y)

def hcf(a, b):
    """
    Function to calculate HCF of two numbers.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: HCF of a and b
    """
    # Loop from minimum number down to 1
    for i in range(z, 0, -1):
        # Check if 'i' divides both numbers
        if a % i == 0 and b % i == 0:
            return i

# Displaying the result
print(f"hcf of {x} and {y} is ", hcf(x, y))
