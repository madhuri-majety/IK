#! /usr/bin/python3

"""
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be
expressed as following recurrence relation.
T(n) = 2T(n/2) + \Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of
Master Method and solution of the recurrence is \Theta(nLogn).
Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always
divides the array in two halves and take linear time to merge two halves.

Auxiliary Space: O(n)

Algorithmic Paradigm: Divide and Conquer

Sorting In Place: No in a typical implementation

Stable: Yes

Applications of Merge Sort

    Merge Sort is useful for sorting linked lists in O(nLogn) time.In case of linked lists the
    case is different mainly due to difference in memory allocation of arrays and linked lists.
    Unlike arrays, linked list nodes may not be adjacent in memory. Unlike array, in linked list,
    we can insert items in the middle in O(1) extra space and O(1) time. Therefore merge operation of merge sort
    can be implemented without extra space for linked lists.

    In arrays, we can do random access as elements are continuous in memory.
    Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i],
    we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list.
    Quick Sort requires a lot of this kind of access. In linked list to access ith index, we have to travel
    each and every node from the head to ith node as we dont have continuous block of memory. Therefore,
    the overhead increases for quick sort. Merge sort accesses data sequentially and the need of
    random access is low.
"""
def merge(arr, st, mid, end):
    """
    Imagine the last leaf in the recursion tree where there is only single elements has to be merged.
    Last leaf node will be merge(arr, st=0, mid=0, end=1) then the logic becomes easy to code.
    :param arr:
    :param st:
    :param mid:
    :param end:
    :return:
    """
    nl = mid - st + 1
    nr = end - mid

    # Create 2 temp arrays
    l = [0] * nl
    r = [0] * nr

    # Copy Data to temp arrays
    for i in range(0, nl):
        l[i] = arr[st + i]

    for j in range(0, nr):
        r[j] = arr[mid + 1 + j]

    # Merge the temp arrays back into arr[st..end]
    i = 0
    j = 0
    k = st

    while i < nl and j < nr:
        if l[i] < r[j]:
            arr[k] = l[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = r[j]
            k = k + 1
            j = j + 1

    # Copy the remaining elements of l if any
    while i < nl:
        arr[k] = l[i]
        k = k + 1
        i = i + 1

    # Copy the remaining elements of r if any
    while j < nr:
        arr[k] = r[j]
        k = k + 1
        j = j + 1

def merge_sort(arr, st, end):
    """

    :param arr:
    :param st:
    :param end:
    :return:
    """
    if st < end:

        # To avoid the overflow of memory
        mid = st + (end-st)//2

        # Sort first and second halves
        merge_sort(arr, st, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, st, mid, end)


list = [1,4,7,21,2,3,5,6]
print("Before sorting the list: ", list)
merge_sort(list, 0, len(list)-1)
print("After merge sorting the list: ", list)



