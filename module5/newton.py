import math


def newton(number):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + number / estimate) / 2
        difference = abs(number - estimate ** 2)
        if difference <= tolerance:
            break

    return estimate


def main():
    number = input("Enter a positive number or enter/return to quit: ")

    while number != "":
        number = float(number)
        square_root = newton(number)

        print("The program's estimate is", square_root)
        print("Python's estimate is", math.sqrt(number))

        number = input("Enter a positive number or enter/return to quit: ")

if __name__ == "__main__":
    main()


