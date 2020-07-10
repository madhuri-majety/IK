#! /usr/bin/python3

"""
Main assumption to this program is that the list elements are unique.
No of rotations = index of the lowest element in the list
Case 1: A[low] <= A[high]: return low
Case 2: Pivot Property - Next and Previous element are greater than mid element
            next <- (mid+1)%N
            previous <- (mid+n-1)%N
            A[mid] <= A[next] && A[mid] >= A[prev]
Case 3: To break the problem into segments if the right element is not found in case1 and case2
        A[mid] <= A[high] (already sorted, search the left segment)
            high = mid-1
Case4: A[low] <= A[mid] (already sorted, search the right segment)
            low = mid+1
"""
def binary_search_rotation_count(list):
    low = 0
    high = len(list)-1
    size = len(list)
    while (low <= high):
        if(list[low] <= list[high]):
            return low
        mid = low + (high-low)//2
        #print("Mid is {}".format(mid))
        next_elem = (mid+1)%size
        #print("Next is {}".format(next_elem))
        prev_elem = (mid+size-1)%size
        #print("Mid is {}".format(prev_elem))

        if ((list[mid] <= list[next_elem]) and (list[mid] <= list[prev_elem])):
            return mid
        elif list[mid] <= list[high]:
            high = mid - 1
        elif list[mid] >= list[low]:
            low = mid + 1
    return None

#ls = [1,2,3,4,6,7,5,9,8,11,10]
ls = [1,1,1,1,1]
sorted_list = sorted(ls)
rotated_ls = [15,22,23,28,31,38,5,6,8,10,12]
count = binary_search_rotation_count(ls)
print("Rotation count of a sorted list is {}".format(count))
