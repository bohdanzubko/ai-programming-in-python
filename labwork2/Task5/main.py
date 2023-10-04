# Factorial function
def fact(a):
    if a == 0 or a == 1:
        return 1
    return a * fact(a - 1)


# Main function
def main():
    n = int(input("Enter N: "))
    a = n + 5
    print(f"({n} + 5)! = ", fact(a))


if __name__ == '__main__':
    main()