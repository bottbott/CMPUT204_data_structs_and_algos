# from ..ryan_heap import heap
import sys
import os
sys.path.append(os.path.abspath('/Users/ryanbott/LocalDocs/School/CMPUT 204/Code/DataStructures')) 
from ryan_heap import heap

arr = [6,5,3,7,9,0,2]
print("before heapifying: ", arr)
h = heap(arr)

h.buildMaxHeap()
print("after heapifying: ", arr)

arr = [2,2,6,6,8,8,9,9,11,11]
print("before heapifying: ", arr)
h = heap(arr)

h.buildMaxHeap()
print("after heapifying: ", arr)