from numpy import random


# Main function
def main():
    n = int(input("Enter N = "))
    array_len = n + 10
    array = random.randint(100, size=array_len)
    print("Generated array:", *array)
    array[0], array[-1] = array[-1], array[0]
    print("New array:", *array)


if __name__ == '__main__':
    main()