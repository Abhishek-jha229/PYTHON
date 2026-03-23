"""
Program: LCM (Least Common Multiple) Finder
-------------------------------------------
Definition:
The Least Common Multiple (LCM) of two numbers is the smallest positive number
that is divisible by both numbers.

Example:
LCM of 4 and 6:
Multiples of 4 → 4, 8, 12, 16...
Multiples of 6 → 6, 12, 18...
Common multiple → 12 (smallest)

Hence, LCM = 12
"""

# Taking input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def lcm(a, b):
    """
    Function to calculate LCM of two numbers

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: LCM of a and b
    """

    # Start from the maximum of the two numbers
    z = max(a, b)

    # Loop from max(a, b) to a*b
    for i in range(z, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


# Edge case handling
if x <= 0 or y <= 0:
    print("Please enter positive integers only")
else:
    result = lcm(x, y)
    print(f"LCM of {x} and {y} is: {result}")
