#! /usr/bin/python3
"""
Main assumption to this program is that the list elements are unique.
Case 1: A[mid] == x : return mid
Case 2: Find if the right segment is sorted
        A[mid] <= A[high]
        Case 2A: x > A[mid] && x <= A[high]
                    low = mid + 1
        Case 2B:    high = mid -1
Case 3: Find if the left segment is sorted
        A[low] <= A[mid]
        Case 3A: x < A[mid] && x >= A[low]
                    high = mid-1
        Case 3B:    low = mid + 1
"""

def circular_array_search(list,value):
    low = 0
    high = len(list)-1
    while(low <= high):
        mid = low + (high-low)//2
        if value == list[mid]:
            return mid
        # Find if the right segment is sorted
        if list[mid] <= list[high]:
            if value > list[mid] and value <= list[high]:
                low = mid + 1
            else:
                high = mid - 1

        # Find if the left segment is sorted
        elif list[low] <= list[mid]:
            if value >= list[low] and value < list[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return None


ls = [12,14,18,21,3,6,8,9]
print("Printing the list: {}".format(ls))

value = input("Enter the value to search is circular sorted list:")
print("Element to search is {}".format(value))

index = circular_array_search(ls, int(value))
if index is not None:
    print("Element {} is found at index {}".format(value,index))
else:
    print("Element is not found")
