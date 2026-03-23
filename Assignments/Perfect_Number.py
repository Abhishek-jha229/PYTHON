"""
Program: Perfect Number Checker
--------------------------------
Definition:
A perfect number is a positive integer that is equal to the sum of its proper divisors,
excluding the number itself.

Example:
6 → Divisors: 1, 2, 3
Sum = 1 + 2 + 3 = 6 → Perfect Number

28 → Divisors: 1, 2, 4, 7, 14
Sum = 28 → Perfect Number
"""

# Taking input from user
x = int(input("Enter the number: "))

def perfect_num(x):
    """
    Function to check whether a number is a perfect number or not

    Parameters:
    x (int): The number to be checked

    Returns:
    None (prints result)
    """

    total = 0  # Variable to store sum of divisors

    # Loop to find divisors from 1 to x-1
    for i in range(1, x):
        if x % i == 0:
            total += i

    # Checking condition
    if total == x:
        print(f"{x} is a Perfect Number")
    else:
        print(f"{x} is NOT a Perfect Number")


# Edge case handling
if x <= 0:
    print("Please enter a positive integer")
else:
    # Function call
    perfect_num(x)
