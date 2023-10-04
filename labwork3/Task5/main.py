from check_sorting import check_sorted


# Replace element of integer array by sum of element and index
def replace_with_index_sum(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] + i
    return arr


# Main function
def main():
    check_dict = {0: 'ascending', 1: 'descending'}
    arr = list(map(int, input("Enter array: ").split()))
    order = int(input("Enter sort type (0 - ascending)/(1 - descending): "))

    if check_sorted(arr, check_dict[order]):
        print("Correct sorting!")
        print("Modified array: ", *replace_with_index_sum(arr))
    else:
        print("Wrong sorting!")


if __name__ == '__main__':
    main()
