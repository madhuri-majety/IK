"""
Max Heap implementation in python
Public functions: push, peek, pop
Private functions: __floatup, __bubbledown, __swap
"""

class MaxHeap():
    def __init__(self, items = []):
        super().__init__()
        self.heap = []
        for i in items:
            self.heap.append(i)
            self.__floatup(len(self.heap) - 1)

    def push(self, data):
        """
        Append the data to the end of the heap and float up the value to the correct index
        For newly created index, calculate the parent node using i-1//2 formula and compare
        If parent is less than current data then swap and float up that node if necessary
        :param data:
        :return:
        """
        self.heap.append(data)
        self.__floatup(len(self.heap) -1)

    def pop(self):
        """
        Swap the root node to the last node, pop the last element which is max element and bubble down the root
        if the max heap invarient is not met
        :return:
        """
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbledown(0)
        elif len(self.heap) == 1:
            max = self.heap.pop()
        else:
            max = False

        return max

    def peek(self):
        """
        Return the root node which is at index 0
        :return:
        """
        if self.heap[0]:
            return self.heap[0]

    def __floatup(self, index):
        """
        For the current index, calculate the parent using the formula (i-1)//2 for 0 based indexing
        Compare the data at current index with parent index and if data at current index is greater then
        swap the data and floatup the parent index
        :param index:
        :return:
        """
        parent = (index -1)//2

        if parent <= 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatup(parent)


    def __bubbledown(self, index):
        """
        For a given node, calculate the left and right child using formula 2i+1, 2i+2
        compare the current index value with its left and right child and if it is less
        than any left or right swap with lesser value and if both are less then swap it with
        max of left and right child and bubble down further with swapped index
        :param index:
        :return:
        """
        left = (2 * index) + 1
        right = (2 * index) + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if index != largest:
            self.__swap(index, largest)
            self.__bubbledown(largest)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


m = MaxHeap([95,3,21])
print(m.peek())
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(m.pop())
print(m.pop())
print(m.pop())
print(m.pop())

