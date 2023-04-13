import math
# recursively defined algorithm 
def mergeSort(arr, start, end):
    # need a base case to exit the dividing
    if (start < end): # the pointers not the arr values must be checked. 
        middle = math.floor((start + end) / 2)
        mergeSort(arr, start, middle) # divide n/2
        mergeSort(arr, middle + 1, end) # divide n/2
        merge(arr, start, middle, end) # conquer/combine

def merge(arr, start, middle, end):
    left_half = arr[start : middle + 1]
    right_half = arr[middle + 1: end + 1]
    
    left_len = middle - start + 1 # could use len, but "slower"
    right_len = end - middle      # could use len, but "slower"

    # init pointers
    i = j = 0
    k = start

    while i < left_len or j < right_len:
        if j >= right_len or (i < left_len and left_half[i] <= right_half[j]):
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j  += 1
        k += 1


def merge_three_loops(array, start, middle, end):
    # Create temp arrays by slicing the original
    left_half = array[start:middle+1]
    right_half = array[middle+1:end+1]

    # init pointers
    i = j = 0
    k = start

    # merge left and right into original array
    # this first loop can at least merge n/2 elements
    # if, it merges in all of the left or all of the right
    # then the next two loops will add in the values that this
    # loop missed. 
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        # Increment k to add the next element to array
        k += 1
    
    # append remaining elements from left_half to arr
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1