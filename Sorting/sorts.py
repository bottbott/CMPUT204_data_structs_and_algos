import random

from insertionSort import insertionSort
from mergeSort import mergeSort
from heapSort import heapSort
from quickSort import quickSort

test_array = [1,7,3,8,7,4,8,9]
print("Before sort: ", test_array)
insertionSort(test_array, len(test_array))
print("insertionSort:", test_array, "\n")


random.shuffle(test_array)
print("Before sort: ", test_array)
mergeSort(test_array, 0, len(test_array) - 1)
print("Mergesort: ", test_array, "\n")

random.shuffle(test_array)
print("Before sort: ", test_array)
heapSort(test_array)
print("Heapsort: ", test_array, "\n")

random.shuffle(test_array)
print("Before sort: ", test_array)
quickSort(test_array, 0, len(test_array) - 1)
print("Quicksort: ", test_array, "\n")