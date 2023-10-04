# Importing math package
from math import *


# Finding point location
def coordinate_area(x, y):
    r = 2
    if ((-1 <= y <= 1) and (-3 <= x <= 3)) and sqrt(x**2 + y**2) <= r:
        return True
    return False


# Main function
def main():
    x, y = float(input("Enter x: ")), float(input("Enter y: "))
    if coordinate_area(x, y):
        print("the point belongs to the area")
    else:
        print("the point does not belongs to the area")


if __name__ == '__main__':
    main()
