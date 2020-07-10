"""
Heap Sort:
    - Inplace Sorting Algorithm with nlogn worst case
    - heap sort is optimal for both time and space, but:
        - Inner loop longer than quicksort
        - Makes poor use of cache
        - Not Stable
Heap sort is a comparison based sorting technique based on Binary Heap data structure.
It is similar to selection sort where we first find the maximum element and place the maximum element at the end.
We repeat the same process for remaining element.

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node
is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is
called min heap. The heap can be represented by binary tree or array.

Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based representation
is space efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and
right child by 2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap
followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

How to build the heap?
Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be
performed in the bottom up order.


Python Built-in methods:
Python has built in heapq library to implement the heap sort
https://docs.python.org/2/library/heapq.html

Time Complexity: O(nlogn)
best = 3n
Average = 2nlogn
Worst = 2nlogn

Auxiliary Space: O(1)

Stable : No


"""
from heapq import heappush, heappop, heapify


def max_heapify(arr, size, index):
    largest = index
    left = (2*index)+1
    right = (2*index)+2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, size, largest)

def min_heapify(arr, size, index):
    smallest = index
    left = (2*index)+1
    right = (2*index)+2

    if left < size and arr[left] < arr[smallest]:
        smallest = left

    if right < size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        min_heapify(arr, size, smallest)


def heap_sort(arr):
    """
    MAX Heap sort always sorts the elements in ascending order.
    :param arr:
    :return:
    """
    n= len(arr)

    for i in range(n//2 -1, -1, -1):
        max_heapify(arr, n, i)
    #print("***: {}".format(arr))
    # Max heap always have the max element on top, so swap it to the last element
    # in the array and heapify the rest of the tree at root.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        #print("%%%: {}".format(arr))
        max_heapify(arr, i, 0)
        #print("&&&:{}".format(arr))

    return arr

def min_heap_sort(arr):
    """
    MIN Heap sort always sorts the elements in descending order.
    :param arr:
    :return:
    """
    n = len(arr)

    # Build min heap for a given data
    # After the for loop ends, the array satisfies the min heap property
    for i in range(n//2 -1, -1, -1):
        min_heapify(arr, n, i)

    # Now actual sorting takes place by swapping the root (min element)
    # to end of the list and heapify rest of the list again
    # So the min to max comes from left to right which is descending order
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)

    return arr


def heapsort_builtin(iterable):
    """
    Using built in methods to implement heapsort.

    heapq.heappush(heap, item)

        Push the value item onto the heap, maintaining the heap invariant.

    heapq.heappop(heap)

        Pop and return the smallest item from the heap, maintaining the heap invariant.
        If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

    :param iterable:
    :return:
    """
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def main():
    print("Using heapq Datastructure")
    print(heapsort_builtin([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    print("Printing using implemented Max Heap sort")
    print(heap_sort(list))

    print("Printing using implemented Min Heap sort")
    print(min_heap_sort(list))

    list2 = [13, 11, 12, 7, 6, 5, 8, 10]
    print("/nPrinting list2 \n")
    print(min_heap_sort(list2))
    # Transform list into a heap, in-place, in linear time. Heap property is that any parent is less than its
    # children. That is the min heap property that python built in heapq data structure does.
    #heapify(list)
    #print("Printing heap list using heapify:", list)

if __name__ == '__main__':
    main()
