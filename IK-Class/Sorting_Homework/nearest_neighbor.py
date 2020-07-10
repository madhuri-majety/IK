"""
Given a point P, and other N points in two dimensional space, find K points out of the N Points which are nearest to P.

Two ways to solve the problem:
- Quick Sort partitioning around the Point P
- Max Heap to pick k nearest points to P
"""

from heapq import heappop, heappush
import time
import random

def get_distance(p1,p2):
    """
    Calulate distance between two points in a two dimensional space
    This distance will be the key factor to find the nearest neighbors
    :param p1:
    :param p2:
    :return:
    """
    return (pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

def nearest_neighbor_max_heap(a, point, k):
    """
    Make a max heap and populate with k elements. Default heap in heapq module is Min heap.
    So make max heap, store negative distance values and min heapify it. That will give the
    max heap representation of distances by ignoring the negative value
    :param a:
    :param point:
    :param k:
    :return:
    """
    heap = []
    for elem in a:
        if len(heap) < k:
            # Insert tuple into heap with negative distance value and the actual element itself to make it max heap
            heappush(heap, (-1 * get_distance(point, elem), elem))
        else:
            curr_distance = get_distance(point, elem)
            if curr_distance < -1 * heap[0][0]:
                heappop(heap)
                heappush(heap, (-1 * curr_distance, elem))

    return [elem[1] for elem in heap]

def nearest_neighbors_qs(a, point, k):
    comp_func = lambda x : get_distance(point, x)
    return nearest_neighbors_qs_util(a, k, 0, len(a)-1, comp_func)

def nearest_neighbors_qs_util(a, k, start, end, comp_func):
    pivot = partition(a, start, end, comp_func)

    if pivot+1 == k:
        return a[:pivot+1]
    elif pivot + 1 > k:
        # Search in the left half of the array
        return nearest_neighbors_qs_util(a, k, start, pivot-1, comp_func)
    else:
        return nearest_neighbors_qs_util(a, k, pivot+1, end, comp_func)

def partition(a, start, end, comp_func):
    # Randomize the partition for best case time complexity
    idx = random.randint(start, end)
    a[idx], a[end] = a[end], a[idx]

    pivot = a[end]
    pindex = start

    for i in range(start, end):
        if comp_func(a[i]) <= comp_func(pivot):
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1

    a[pindex], a[end] = a[end], a[pindex]

    return pindex

def main():
    P = (0, 0)
    arr = [(2, 0), (1, 5), (1, 7), (0, -1), (7, 4), (5, 7), (8, 5), (4, 9)]
    k = 4
    start_time = time.time()
    print(nearest_neighbor_max_heap(arr, P, k))
    print("Elapsed time for Heap: {}".format(time.time() - start_time))
    start_time = time.time()
    print(nearest_neighbors_qs(arr, P, k))
    print("Elapsed time for QS: {}".format(time.time() - start_time))
    print('\n')



    arr = [(1, -3), (1, 2), (3, 4)]
    print(nearest_neighbor_max_heap(arr, P, 1))
    #print(nearest_neighbors_qs(arr, P, 1))
    print('\n')

    arr = [(3, 6), (2, 4), (5, 3), (2, 7), (1, 8), (7, 9)]
    #print(nearest_neighbors_qs(arr, P, 3))
    print(nearest_neighbor_max_heap(arr, P, 3))

if __name__ == '__main__':
    main()