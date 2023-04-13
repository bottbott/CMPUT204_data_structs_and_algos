from tree import Tree

class heap(Tree):
    def __init__(self, arr):
        self.heapsize = 0
        self.arr = arr

    def left(self, i):
        return (2 * (i + 1)) - 1
    
    def right(self, i):
        return (2 * (i + 1))
        # return (2 * i + 1) - 1 + 1
    
    def buildMaxHeap(self):
        self.heapsize = len(self.arr)
        for i in range(self.heapsize // 2 - 1, -1, -1):
            self.maxHeapify(i)

    def maxHeapify(self, i):
        leftChild = self.left(i)
        rightChild = self.right(i)

        largest = i

        if (leftChild <= self.heapsize - 1 and self.arr[leftChild] > self.arr[largest]):
            largest = leftChild
        if (rightChild <= self.heapsize - 1 and self.arr[rightChild] > self.arr[largest]):
            largest = rightChild
        if (largest != i):
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.maxHeapify(largest)