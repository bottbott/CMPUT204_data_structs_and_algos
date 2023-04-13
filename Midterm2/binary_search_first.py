import math
A = [2,3,5,8,9,9,10]

def FirstOccur(x, array, start, end):
    half_index = math.floor(len(array)/2)
    found = -1
    if len(array) == 0 or found != -1:
        return -1
    if array[half_index] == x and array[half_index] > array[half_index - 1]:
        return half_index
    
    
    found = FirstOccur(x, A[start:half_index-1], start, half_index-1)
    if found == -1:
        found = FirstOccur(x, A[half_index +1:end], half_index+1, end)

    return found


print(FirstOccur(9, A, 0, 6))