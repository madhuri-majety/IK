import random

"""
Analysis of QuickSort
Time taken by QuickSort in general can be written as following.

 T(n) = T(k) + T(n-k-1) + theta(n)

The first two terms are for two recursive calls, the last term is for the partition process.
k is the number of elements which are smaller than pivot.
The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot.
If we consider above partition strategy where last element is always picked as pivot, the worst case would occur
when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.

 T(n) = T(0) + T(n-1) + theta(n)
which is equivalent to
 T(n) = T(n-1) + theta(n)

The solution of above recurrence is theta(n2).

Best Case: The best case occurs when the partition process always picks the middle element as pivot.
Following is recurrence for best case.

 T(n) = 2T(n/2) + theta(n)

The solution of above recurrence is theta(nLogn). It can be solved using case 2 of Master Theorem.

Average Case:
To do average case analysis, we need to consider all possible permutation of array and calculate time taken
by every permutation which doesnt look easy.
We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set
and O(9n/10) elements in other set. Following is recurrence for this case.

 T(n) = T(n/9) + T(9n/10) + theta(n)

Solution of above recurrence is also O(nLogn)

Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting
algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be
efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in
different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data.
However, merge sort is generally considered better when data is huge and stored in external storage.
"""

def hoares_partition(arr, st, end):
    """
    This is hoare's way of paritioning with two pointers.
    Advantage: Less number of swaps compared to Lomuto's partitioning
    :param arr:
    :param st:
    :param end:
    :return:
    """
    lt = st+1
    rt = end
    pivot = arr[st]

    while(lt < rt):
        while(lt <= end and arr[lt] <= pivot):
            lt += 1
        while(rt >= st and arr[rt] > pivot):
            rt -= 1
        if lt < rt:
            arr[lt], arr[rt] = arr[rt], arr[lt]
    arr[rt], arr[st] = arr[st], arr[rt]
    return rt


def partition(arr, st, end):
    """
    This is Lomuto's partitioning
    Will pick the last element of the list to be the pivot
    Traverse from starting(pindex) of the list until end-1 and compare the value with pivot and if value is less
    than pivot swap it with pindex and increament pindex

    :param arr:
    :param st:
    :param end:
    :return:
    """
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


def quick_sort_Lomuto(arr, st, end):
    if (st < end):
        pindex = randomized_partition(arr,st,end)
        #pindex = partition(arr, st, end)
        quick_sort_Lomuto(arr, st, pindex-1)
        quick_sort_Lomuto(arr, pindex+1, end)

def quick_sort_Hoare(arr, st, end):
    if (st < end):
        pindex = hoares_partition(arr,st,end)
        quick_sort_Hoare(arr, st, pindex-1)
        quick_sort_Hoare(arr, pindex+1, end)


list = [1,4,7,21,2,2,5,6]
print("Before sorting the list: ", list)
quick_sort_Lomuto(list, 0, len(list)-1)
print("After quick sorting the list using Lomuto Partiotioning: ", list)

list1 = [3,4,7,21,2,2,5,6]
print("Before sorting the list: ", list1)
quick_sort_Hoare(list1, 0, len(list1)-1)
print("After quick sorting the list using Hoare Partiotioning: ", list1)
