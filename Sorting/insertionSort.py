# iterively defined algorithm 
def insertionSort(array, size):
    size = len(array)
    # iteration over 
    for j in range(2, size):
        # begin with each ith element as our key and then put it in our sorted sub-array
        key = array[j]
        i = j - 1
        while (i > 0 and array[i] > key):
            # shift all of the elements up from 
            array[i+1] = array[i]
            i = i - 1
        # put key in position
        array[i + 1] = key


