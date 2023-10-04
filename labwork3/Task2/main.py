# Multiplication of the first q elements of the arithmetic progression
def arithmetic_mult(a1: float, t: float, q: int) -> float:
    ak = a1
    mult = 1
    for i in range(q):
        mult *= ak
        ak += t
    return mult


def main():
    a1, t, q = float(input("Enter a1: ")), float(input("Enter t: ")), int(input("Enter q: "))

    mult = arithmetic_mult(a1, t, q)
    print(f"The multiplication of the first {q} elements of the arithmetic progression\n"
          f"with the initial element {a1} and the step {t} is {mult}")


if __name__ == "__main__":
    main()
