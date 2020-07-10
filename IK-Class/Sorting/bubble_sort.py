#!/ usr/bin/python3
"""
Bubble sort is the simplest algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order
For every pass, the max element in the unsorted subarrqy is always in the right position

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes

No Of Swaps = O(n*n)


Recursive Bubble Sort:
-----------------------

Recursive Bubble Sort has no performance/implementation advantages, but can be a good question to check ones
understanding of Bubble Sort and recursion.

Recursion Idea:
    Base case: Return if size of the array is 1
    Do one pass of normal bubble sort, this pass fixes the last element of current subarray
    Recur for all elements except last of current subarray
"""
def bubble_sort(list):
    size = len(list)
    for k in range(size):
        flag = 0
        for i in range(0, size-k-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                flag = 1
        if flag==0:
            break

def bubble_sort_rec(list, n):
    if n == 1:
        return
    for i in range(0, n-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            #print(list[i], list[i+1])
    bubble_sort_rec(list, n-1)

list = [2,7,4,1,5,3]
list1 = ["Madhu", "Ritu", "Sumanth", "Rithika", "Jaya"]
list = [1,1,1,1,1,1,2,2,2,2,2]
print("Before sorting the list", list)
bubble_sort(list)
print("After sorting the list", list)

print("Before sorting the list recursively", list1)
bubble_sort_rec(list1, len(list1))
print("After sorting the list recursively", list1)
