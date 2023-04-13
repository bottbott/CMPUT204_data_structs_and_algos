import math
# turn an array into a heap
def build_a_heap(array):
    heap_size = len(array)
    for i in reversed(range(math.floor(len(array)/2))):
        max_heapify(array, heap_size-1, i)

def max_heapify(array, heap_size, i):
    l = get_left(i)
    r = get_right(i)
    if l <= heap_size and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)
    
def get_parent(i):
    return math.floor((i-1)/2)

def get_left(i):
    return 2*i+1

def get_right(i):
    return 2*i+2