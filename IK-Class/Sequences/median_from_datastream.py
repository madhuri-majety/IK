"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.



Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

https://leetcode.com/problems/find-median-from-data-stream/solution/

"""

import heapq

class MedianFinderSorting(object):
    """
    Using simple Sorting
    Store the numbers in a resize-able container. Every time you need to output the median, sort the container and output the median.

    Time Complexity = O(nlogn) + O(1)
    Sorting = O(nlogn)
    Adding number takes amortized O(1) time for a python list with an efficient resizing mechanism
    """
    def __init__(self):
        self.store = []

    def addNum(self, num):
        self.store.append(num)

    def findMedian(self):
        self.store.sort()
        n = len(self.store)
        if n%2 == 0:
            return (self.store[n//2 - 1]+self.store[n//2])*0.5
        else:
            return self.store[n//2]

class MedianFinderBinaryInsertion(object):
    """
    In this algorithm, we insert the new element in the right position using binary search
    find median is still returning the middle elements
    Time Complexity : O(logn) + O(n) ==> O(n)
    """
    def __init__(self):
        self.store = []

    def _find_location_using_binary_search(self, arr, val, start, end):
        # Base cases:
        if start == 0:
            return start

        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1
        if start > end:
            return start

        mid = (start + end)//2

        if arr[mid] < val:
            return self._find_location_using_binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return self._find_location_using_binary_search(arr, val, start, mid-1)
        else:
            return mid

    def add_num(self,num):
        j = self._find_location_using_binary_search(self.store, num, 0, len(self.store))
        self.store.insert(j, num)

    def find_median(self):
        n = len(self.store)
        if n % 2 == 0:
            return (self.store[n//2 - 1] + self.store[n//2])*0.5
        else:
            return self.store[n//2]

class MedianFinderTwoHeaps(object):
    """
    * Lower half of elements will be stored in Max heap & Upper half of elements will be stored in Min Heap with self balancing property
    * At any point max heap and min heap will differ by max 1 element in max heap(lower half)
    Time Complexity =
    O(5 * logN) ==> O(logN)
    """
    def __init__(self):
        self.lower_half_max_heap = []
        self.higher_half_min_heap = []

    def add_num(self, num):
        # Insert the element into lower half all the time which is max heap
        # As python has only minheap, we need to store the negative values in max heap
        heapq.heappush(self.lower_half_max_heap, -1*num)

        # Push the max element in lower half to higher half min heap
        move_higher = -heapq.heappop(self.lower_half_max_heap)
        heapq.heappush(self.higher_half_min_heap, move_higher)

        # Check for the size property where lower array will 1 higher than higher array
        if len(self.lower_half_max_heap) < len(self.higher_half_min_heap):
            move_lower = heapq.heappop(self.higher_half_min_heap)
            heapq.heappush(self.lower_half_max_heap, -1*move_lower)

    def find_median(self):
        if len(self.lower_half_max_heap) > len(self.higher_half_min_heap):
            return (-self.lower_half_max_heap[0])
        else:
            return (-self.lower_half_max_heap[0] + self.higher_half_min_heap[0])*0.5


def main():
    print("Finding Median using Simple Sorting")
    mfs = MedianFinderSorting()
    mfs.addNum(1)
    mfs.addNum(2)
    print(mfs.findMedian())
    mfs.addNum(3)
    print(mfs.findMedian())

    print("Finding Median using Binary Insertion Sort")
    mfbi = MedianFinderBinaryInsertion()
    mfbi.add_num(1)
    print(mfbi.find_median())
    mfbi.add_num(2)
    print(mfbi.find_median())
    mfbi.add_num(3)
    print(mfbi.find_median())

    print("Finding Median using Two heap solution")
    mfh = MedianFinderTwoHeaps()
    mfh.add_num(1)
    print(mfh.find_median())
    mfh.add_num(2)
    print(mfh.find_median())
    mfh.add_num(3)
    print(mfh.find_median())


if __name__ == '__main__':
    main()




