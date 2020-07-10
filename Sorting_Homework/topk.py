"""
Find K largest elements in the stream of input

*********** Crux: Use Min heap to find top k largest *****************

https://docs.python.org/2/library/heapq.html

https://github.com/python/cpython/blob/2.7/Lib/heapq.py

Solution#6:
https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/



https://www.careercup.com/question?id=5644780193185792

For "K largest elements":
--------------------------
There are 4 solutions worth discussing:

Solution #1. Min-Heap solution with O(N log K) time, O(K) extra space:
Use a min heap of size at most K to store elements. Keep inserting element into the min heap.
When the size is K+1, we know that the minimum element in the heap will always smaller than at least K other elements
(also in the min heap now). Thus, that minimum element must be extracted from the heap, maintaining the heap size
of at most K.


Solution #2. Max Heap solution, with O(K log N) time, O(N) space:
Use a max heap of size N. Making a heap (e.g., max heap) from an array of size N can be done in O(N) time,
no extra space. After making such a max heap of size N, just extract K elements from it to get K largest elements,
in O(K log N) time.

Note, when K<<N, K log N is also << N log K. Therefore, the max-heap solution has better time complexity than the
min-heap solution.


Solution #3. Algorithm via quick select idea:
- Find the K-th largest element X using quick select, in O(N) time.
- Partition the array into 2 parts, using X as the pivot, in O(N) time. Suppose the left part contains all K numbers >= X.
- Sort the left part, using most efficient sorting algorithm, which takes f(K) time.

Time complexity: O(N + f(K)). Where f(K) = K if using linear time sorting algorithm,
or f(K) = K log K if use comparison-based sorting algorithm, like merge sort.


Solution #4. Algorithm via sorting:
- Sort the array;
- Print first K largest elements.

Complexity of sorting algorithms can be:
- O(N log N), if use best comparison-based sorting algorithm like merge short;
- O(N*L) if use radix sort, where L = length of the largest element, can consider L = O(1);
- O(N + M) if use counting sort, where M = value of the largest element.


My order of preference (based on time complexity and easiness of implementation):
1. radix sort, if O(N) extra space is allowed;
2. max-heap, if modification on original array is allowed (for make_heap()), or O(N) extra space is allowed;
3. min-heap, if O(K) space is allowed;
4. partitioning via quick select (not trivial implementation).
"""

import heapq

def topk(arr, k):
    return heapq.nlargest(k, arr)

def topk_minheap(arr, k):
    """
    Method 6 (Use Min Heap)  ==> Best Solution
    This method is mainly an optimization of method 1. Instead of using temp[] array, use Min Heap.

    1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

    2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
        ……a) If the element is greater than the root then make it root and call heapify for MH
        ……b) Else ignore it.
    // The step 2 is O((n-k)*logk)

    3) Finally, MH has k largest elements and root of the MH is the kth largest element.

    Time Complexity: O(k + (n-k)Logk) without sorted output. If sorted output is needed then O(k + (n-k)Logk + kLogk)

    All of the above methods can also be used to find the kth largest (or smallest) element.
    :param arr:
    :param k:
    :return:
    """
    h = []
    # Read k elements from list and push it to heap datastructure. This will maintain the min heap invariant.
    for i in range(k):
        heapq.heappush(h, arr[i])

    # For each element after the kth elementm compare it with root and if it is greater than root, then replace the root
    # with element from list and heapify it again.
    for i in range(k, len(arr)):
        if arr[i] > h[0]:
            h[0] = arr[i]
            heapq.heapify(h)

    return(h)

def max_heapify(arr, size, index):
    """
    Solution #2. Max Heap solution, with O(K log N) time, O(N) space:
    Use a max heap of size N. Making a heap (e.g., max heap) from an array of size N can be done in O(N) time,
    no extra space. After making such a max heap of size N, just extract K elements from it to get K largest elements,
    in O(K log N) time.

    Note, when K<<N, K log N is also << N log K. Therefore, the max-heap solution has better time complexity than the
    min-heap solution.

    ISSUE: max-heap, if modification on original array is allowed (for make_heap()), or O(N) extra space is allowed;

    Time Complexity:  O(K log N)

    :param arr:
    :param size:
    :param index:
    :return:
    """
    largest = index
    left = (2*index)+1
    right = (2*index)+2

    if left < size and arr[largest] < arr[left]:
        largest = left

    if right < size and arr[largest] < arr[right]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, size, largest)


def topk_maxheap(arr, k):

    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

    result = []
    for i in range(n-1, n-k-1, -1):
        result.append(arr[0])
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

    return result



def main():

    print("Enter the value of k:")
    k = int(input())

    list = [10, 50, 40, 5, 6, 45]
    print("Printing top k elements using built-in method:", topk(list, k))
    print("Printing actual list passed to built-in heap method:", list)

    list2 = [10,4,3,2,11,15,1,16]
    print("Printing top k elements using min heap method:", topk_minheap(list2, k))
    print("Printing actual list passed to MIN heap method:", list2)

    list3 = [10, 4, 3, 2, 11, 15, 1, 16]
    print("Printing top k elements using max heap method:", topk_maxheap(list3, k))
    # By using max heap method, we are changing the order of elements in actual array/list
    print("Printing actual list passed to MAX heap method:", list3)


if __name__ == '__main__':
    main()
