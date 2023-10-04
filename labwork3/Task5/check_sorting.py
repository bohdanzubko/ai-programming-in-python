# Check the type of sorting in integer array by using order from dictionary
def check_sorted(arr, order):
    n = len(arr)
    if order == 'ascending':
        return all(arr[i] <= arr[i+1] for i in range(n-1))
    elif order == 'descending':
        return all(arr[i] >= arr[i+1] for i in range(n-1))
    else:
        raise ValueError("Invalid order value, must be 0 (ascending) or 1 (descending)")
