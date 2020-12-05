# Modify the code below
"""
File: newton.py
Project 6.1
Compute the square root of a number (uses function with loop).
1. The input is a number, or enter/return to halt the
   input process.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math


# Initialize the tolerance
TOLERANCE = 0.000001

def newton(number, estimate):
    """Returns the square root of x."""
    # Perform the successive approximations
    estimate = (estimate + number / estimate) / 2
    difference = abs(number - estimate ** 2)

    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(number, estimate)


def main():
    """Allows the user to obtain square roots."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        estimate = 1.0
        print("The program's estimate is", newton(x, estimate))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()