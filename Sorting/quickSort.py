def quickSort(arr, start, end):
    if (start < end):
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end): # range is -1 at the last element, so don't need - 1 from pseudocode. 
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1