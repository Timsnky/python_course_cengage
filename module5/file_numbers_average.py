
def format_number(numbers):
    for index in range(len(numbers)):
        numbers[index] = float(numbers[index])

    return numbers


def get_sum(numbers):
    return sum(numbers)


def process_numbers(format_number, numbers):
    return format_number(numbers)


def calculate_average(get_sum, numbers):
    if len(numbers) == 0:
        return 0

    return get_sum(numbers) / len(numbers)


def main():
    input_file = input("Enter the input file name: ")
    numbers = []

    f_input = open(input_file, "r")
    for line in f_input:
        numbers.extend(process_numbers(format_number, line.split(" ")))

    print("The average is", calculate_average(get_sum, numbers))


if __name__ == "__main__":
    main()