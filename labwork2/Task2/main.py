# Importing math package
from math import *


# Solution of equation with the condition
def equations(x, a):
    if x < 0:
        return -a * sqrt(1 - x**2 / (4 * a**2))
    else:
        return a / (2 * (e ** (x/a) + e ** (-x/a)))


# Main function
def main():
    x, a = float(input("Enter x: ")), float(input("Enter a: "))
    print("{0:.4f}".format(equations(x, a)))


if __name__ == '__main__':
    main()
