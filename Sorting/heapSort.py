import sys
import os
sys.path.append(os.path.abspath('/Users/ryanbott/LocalDocs/School/CMPUT 204/Code/DataStructures')) 
from ryan_heap import heap



def heapSort(arr):
    h = heap(arr)
    h.buildMaxHeap()

    for i in range(h.heapsize - 1, 1 - 1, -1):
        print(i)
        arr[0], arr[i] = arr[i], arr[0]
        h.heapsize = h.heapsize - 1
        h.maxHeapify(0)