# Check the type of sorting in integer array by using order from dictionary
def check_sorted(arr, order):
    n = len(arr)
    if order == 'ascending':
        return all(arr[i] <= arr[i+1] for i in range(n-1))
    elif order == 'descending':
        return all(arr[i] >= arr[i+1] for i in range(n-1))
    else:
        raise ValueError("Invalid order value, must be 0 (ascending) or 1 (descending)")


# Main function
def main():
    check_dict = {0: 'ascending', 1: 'descending'}
    arr = list(map(int, input("Enter array: ").split()))
    order = int(input("Enter sort type (0 - ascending)/(1 - descending): "))

    if check_sorted(arr, check_dict[order]):
        print("Correct sorting!")
    else:
        print("Wrong sorting!")


if __name__ == '__main__':
    main()
