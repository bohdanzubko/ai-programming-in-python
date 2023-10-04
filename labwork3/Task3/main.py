# Multiplication of the first q elements of the arithmetic progression
def sum_geom_progression(a1: float, t: float, alim: float) -> float:
    s = a1
    ak = a1
    while ak > alim:
        ak /= t
        s += ak
    return s


# Main function
def main():
    a1, t, alim = float(input("Enter a1: ")), float(input("Enter t: ")), float(input("Enter alim: "))

    total_sum = sum_geom_progression(a1, t, alim)
    print("Total sum of decreasing geometric progression: ", total_sum)


if __name__ == "__main__":
    main()
