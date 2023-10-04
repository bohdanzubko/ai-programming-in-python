# Importing math package
from math import *


# Finding triangle area
def area(a, b, c):
    t_p = (a + b + c) / 2
    t_area = sqrt(t_p * (t_p - a) * (t_p - b) * (t_p - c))
    return t_area


# Expression
def expression(a, x, alf):
    y = (cos(4 * alf) - log(x + a) ** 2 * e ** x * x ** 3 - 1.7 * 10 ** 5 * a) / \
        (x * (x ** 3 + 5) + x ** (a ** 2) - a * sqrt(x - 0.5 * 10 ** (-1.5)))
    return y


# Main function
def main():
    a, b, c = 14, 18, 22
    print(f"Task 1:\na = 14, b = 18, c = 22\n\tTriangle area = {round(area(a, b, c), 2)}\n")
    a, x, alf = 0.5, 3.4, 1.65
    print(f"Task 2:\na = 0.5, x = 3.4, alf = 1.65\n\tResult = {round(expression(a, x, alf), 2)}")


if __name__ == '__main__':
    main()
