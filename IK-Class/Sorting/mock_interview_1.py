"""
Given an array the unsorted number is exactly k elements away
Sort a K sorted array or nearly sorted array

Given an array of n elements, where each element is at most k away from its target position,
devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2,
an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time (See this GFact)
2) One by one remove min element from heap, put it in result array, and add a new element to heap from remaining elements.

Removing an element and adding a new element to min heap will take Logk time. So overall complexity will be O(k) + O((n-k)*logK)

"""

import heapq

def unsorted_k_heap(a, k):
    h = []
    result = []

    print("Original List: {}".format(a))
    for i in range(len(a)):
        if len(h) < k:
            heapq.heappush(h, a[i])
            #print("Heap after initial push: {}".format(h))
        else:
            #print("New element coming in is {}".format(a[i]))
            #print("Root of heap is {}".format(h[0]))
            if a[i] > h[0]:
                result.append(heapq.heappop(h))
                heapq.heappush(h, a[i])
                #print("Heap after adding new element: {}".format(h))
            else:
                #print("Same value as heap root")
                result.append(a[i])

    while h:
        result.append(heapq.heappop(h))

    return result


print(unsorted_k_heap([1,5,3,4,2,6], 3))
print(unsorted_k_heap([1,1,1,1,1,1], 3))
print(unsorted_k_heap([6,5,3,4,2,1], 6))
