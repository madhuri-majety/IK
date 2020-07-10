"""
Insertion sort using binary search
We can use binary search to reduce the number of comparisons in normal insertion sort.
Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration.
In normal insertion sort, it takes O(n) comparisons(at nth iteration) in worst case. We can reduce it to O(log n) by using binary search.

*** Base cases are very important here:
Case 1:
If start index == end index - Then compare the index value and actual val and return proper location
If start > end, the two pointers crosses the boundary, so return start index

Time Complexity = O(logN) + O(N^2) ==> O(N^2)
"""

def binary_search_location(arr, val, start, end):

    # Base Case: If the start index and end index meet that means we found out location
    # or if the end crosses the start then we didn't find the match so return start
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end)//2

    if arr[mid] < val:
        return binary_search_location(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search_location(arr, val, start, mid-1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search_location(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr


def main():
    print(insertion_sort([37,23,0,17,12,72,31,46,100,88,54]))

if __name__ == '__main__':
    main()


