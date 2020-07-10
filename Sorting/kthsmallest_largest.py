"""
Kth's smallest/largest element in unsorted array

Given an array ans number k where k is smaller then size of the array, we need to find the k'ths smallest element
in the given array, It is given that all array elements are distinct

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10

Method 1: (Brute Force)
Using Merge sort or Heap sort, sort the array and return the element at index k-1 in the sorted array.
TC - O(nlogn)

Method2: Using Min Heap
Create a min heap of the given elements - O(N) and call extractMin() k times
TC = O(N+ klogN)
SC = O(N) for new max heap

Method3: Using Max Heap
1. Build Max heap of the first k elements of the given array - O(K)
2. For each element, after the kthe element, compare it with root of Max heap
    - If the element is less then the root, make it root and call heapify for max heap
    - Else ignore it.
    TC = O((n-k) logk)

3. Finally the root fo the max heap is the kth smallest element
TC = O(k + (n-k)logk)
SC = O(K)

Method4: QuickSelect
In quicksort, pick the pivot, move the pivot to right position and partition the array around it.
The idea is to not to complete the quicksort, but stop at the point where pivot itself is the kths smallest element.
Also not to recur both left and right sides of pivot, but recur for one of them according to the comparison of k with
position of the pivot

Worst time TC is O(n^2)
Can be made best using radomized pivot or median as the pivot

SC - O(1)

"""

import heapq
import random

def kthsmallest_minheap_builtin(arr, k):
    h = []
    for i in arr:
        heapq.heappush(h, i)

    for i in range(k-1):
        heapq.heappop(h)

    return heapq.heappop(h)

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

def kthsmallest_max_heap_select(arr, k):
    n = len(arr)
    h = []
    for i in range(k):
        h.append(arr[i])

    for i in range((len(h))//2 - 1, -1 ,-1):
        max_heapify(h, len(h), i)

    for i in range(k, n):
        if arr[i] < h[0]:
            h[0] = arr[i]
            max_heapify(h, len(h), 0)

    # Return root
    return h[0]

def partition(arr, start, end):
    pindex = start
    pivot = arr[end]

    for i in range(start,end):
        if arr[i] <= pivot:
            arr[pindex], arr[i] = arr[i], arr[pindex]
            pindex = pindex+1

    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex

def kthsmallest_quickselect_util(arr, st, end, kindex):
    if st >= end:
        print("Entered base condition")
        return arr[kindex]
    else:
        pindex = partition(arr,st,end)

        if pindex == kindex:
            print("Entered recursive return")
            return arr[pindex]
        elif pindex > kindex:
            return kthsmallest_quickselect_util(arr, st, pindex-1, kindex)
        else:
            return kthsmallest_quickselect_util(arr, pindex+1, end, kindex)

def kthsmallest_quickselect(arr, k):
    start = 0
    end = len(arr)-1
    # Kth smallest element will be in k-1 index
    kindex = k-1
    return kthsmallest_quickselect_util(arr, start, end, kindex)

def main():
    k = int(input("Enter the value of k:"))

    list1 = [10, 4, 3, 2, 11, 15, 1, 16]

    print("Printing kth smallest number using Min heap built-in method:", kthsmallest_minheap_builtin(list1, k))

    list2 = [10, 4, 3, 2, 11, 15, 1, 16]

    print("Printing kth smallest number using MAX heap select method:", kthsmallest_max_heap_select(list2, k))

    list3 = [10, 4, 3, 2, 11, 15, 1, 16]
    #list3 = [7, 10, 4, 3, 20, 15]

    print("Printing kth smallest number using Quick select method:", kthsmallest_quickselect(list3, k))


if __name__ == '__main__':
    main()