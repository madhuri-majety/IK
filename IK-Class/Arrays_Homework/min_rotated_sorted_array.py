"""
Find the minimum value in the rotated sorted array
Optimal solution that uses only constant space

A simple solution is to traverse the complete array and find minimum. This solution requires ?(n) time.
We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out following pattern:

    The minimum element is the only element whose previous is greater than it. If there is no previous element element, then there is no rotation
    (first element is minimum). We check this condition for middle element by comparing it with (mid-1)th and (mid+1)th elements.
    If minimum element is not at middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
        If middle element is smaller than last element, then the minimum element lies in left half
        Else minimum element lies in right half.

https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/

"""

def find_min_rotated_sorted_array_recursive(arr, low, high):
    # This condition is needed to handle when array is not
    # rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    #Find Mid
    mid = low + (high - low)//2

    # Check if element mid+1 is minimum element,
    # Consider the case like [3,4,5,1,2]
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]

    # Check if mid itself is minimum element
    if mid > low and arr[mid-1] > arr[mid]:
        return arr[mid]

    # Decide whether we need to go left half or right half
    if arr[high] > arr[mid]:
        return find_min_rotated_sorted_array_recursive(arr, low, mid-1)
    else:
        return find_min_rotated_sorted_array_recursive(arr, mid+1, high)

def find_min_rotated_sorted_array(arr):
    low = 0
    high = len(arr)-1
    print(find_min_rotated_sorted_array_recursive(arr, low, high))

def binary_search_rotation_count(list):
    low = 0
    high = len(list)-1
    size = len(list)
    while (low <= high):
        if(list[low] <= list[high]):
            return list[low]
        mid = low + (high-low)//2
        #print("Mid is {}".format(mid))
        next_elem = (mid+1)%size
        #print("Next is {}".format(next_elem))
        prev_elem = (mid+size-1)%size
        #print("Mid is {}".format(prev_elem))

        if ((list[mid] <= list[next_elem]) and (list[mid] <= list[prev_elem])):
            return list[mid]
        elif list[mid] <= list[high]:
            high = mid - 1
        elif list[mid] >= list[low]:
            low = mid + 1
    return None

def main():
    arr = [6,5,1,2,3,4]
    arr1 = [3, 4, 5, 1, 2]
    arr2 = [70,10,20,30,40,50,60]
    arr3 = [1,1]
    find_min_rotated_sorted_array(arr2)
    print("\n\nPrining using Binary search rotation count method")
    print(binary_search_rotation_count(arr2))

if __name__ == '__main__':
    main()


