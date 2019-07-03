class MinHeap:
    def __init__(self):
        self.heap = [None]
    
    def getParent(self, index):
        return index // 2

    def getLeft(self, index):
        return 2 * index
    
    def getRight(self, index):
        return 2 * index + 1
    
    def insert(self, val):
        self.heap.append(val)

        self.siftUp(len(self.heap) - 1)
    
    def siftUp(self, index):
        if index == 1: return
        
        parentIndex = self.getParent(index)

        if self.heap[parentIndex] > self.heap[index]:
            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            self.siftUp(parentIndex)
    
    def extract(self):
        if len(self.heap) == 1: return None
        if len(self.heap) == 2: return self.heap.pop()

        value = self.heap[1]

        self.heap[1] = self.heap.pop()

        self.siftDown(1)

        return value

    def siftDown(self, index):
        if index 
        
        leftIndex = self.getLeft(index)
        rightIndex = self.getRight(index)
        leftNum = self.heap[leftIndex] if leftIndex < len(self.heap) else float('inf')
        rightNum = self.heap[rightIndex] if rightIndex < len(self.heap) else float('inf')

        swapIndex = None

        if leftNum > self.heap[index] and rightNum > self.heap[index]: return

        if leftNum < rightNum:
            swapIndex = leftIndex
        else:
            swapIndex = rightIndex

        self.heap[index], self.heap[swapIndex] = self.heap[swapIndex], self.heap[index]

        self.siftDown(swapIndex)
