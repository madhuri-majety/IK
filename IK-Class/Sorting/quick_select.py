import random

"""
quickselect is a selection algorithm to find the kth smallest element in an unordered list. 
It is related to the quicksort sorting algorithm.
"""


def partition(arr, st, end):
    """
    Will pick the last element of the list to be the pivot
    Traverse from starting(pindex) of the list until end-1 and compare the value with pivot and if value is less
    than pivot swap it with pindex and increament pindex

    :param arr:
    :param st:
    :param end:
    :return:
    """
    print(end)
    pivot = arr[end]
    pindex = st

    for i in range(st, end):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex = pindex+1
    arr[pindex], arr[end] = arr[end], arr[pindex]

    return pindex

def randomized_partition(arr, st, end):
    """
    Quicksort's worst case time complexity can almost/always be avoided by using what we call
    randomized version of quicksort
    Worst case happens due to unbalanced partition of the array.
    :param arr:
    :param st:
    :param end:
    :return:
    """
    idx = random.randint(st,end)
    arr[idx], arr[end] = arr[end], arr[idx]
    return partition(arr,st,end)


def quick_select(arr, st, end, kindex):
    """
    Returns the k-th smallest element of list within left..right inclusive
    (i.e. left <= k <= right)
    The search space within the array is changing for each round - but the list
    is still the same size. Thus, k does not need to be updated with each round.
    :param arr:
    :param st:
    :param end:
    :return:
    """
    if st >= end:
        print("Entered base condition")
        return arr[kindex]
    else:
        #pindex = randomized_partition(arr,st,end)
        pindex = partition(arr,st,end)
        print(pindex, kindex)

        if pindex == kindex:
            print("Entered recursive return")
            return arr[pindex]
        elif pindex > kindex:
            print("First elif", st, pindex-1, kindex)
            return quick_select(arr, st, pindex-1, kindex)
        else:
            print("Second elif", pindex+1, end, kindex)
            return quick_select(arr, pindex+1, end, kindex)


list = [7, 10, 4, 3, 20, 15]
list1 = [10, 4, 3, 2, 11, 15, 1, 16]
print("Before sorting the list: ", list1)
k = 2
kindex = k-1
kth_smallest_element = quick_select(list1, 0, len(list1)-1, kindex)
print("List after quick selecting is : ", list1)
print("Kth Smallest element is: ", kth_smallest_element)