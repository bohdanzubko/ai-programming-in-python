# Convert decimal digit to binary form
def convert_to_binary(decimal: int):
    binary = count = 0
    while decimal != 0:
        binary += int(decimal % 2) * 10 ** count
        decimal /= 2
        count += 1
    return binary


# Counting "ones" in binary digit
def num_of_ones(number: int):
    counter = 0
    while number != 0:
        if number % 10 == 1:
            counter += 1
        number //= 10
    return counter


# Main function
def main():
    decimal = int(input("Enter unsigned integer number: "))
    binary = convert_to_binary(decimal)
    print("Binary: ", binary)
    print("Count of \"1\": ", num_of_ones(binary))


if __name__ == '__main__':
    main()