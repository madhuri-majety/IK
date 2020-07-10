"""
Given an array arr[], the task is to find the maximum distance between two unequal elements of the given array.

Examples:

Input: arr[] = {3, 2, 1, 2, 1}
Output: 4
The maximum distance is between the first and the last element.

Input: arr[] = {3, 3, 1, 3, 3}
Output: 2

https://www.geeksforgeeks.org/maximum-distance-between-two-unequal-elements/

"""
import sys

def max_distance_bet_unequal_elements_loops(arr, n):
    max_distances = []
    max_dis = -sys.maxint
    if arr[0] != arr[n-1]:
        return n-1

    for i in range(n):
        for j in range(i, n):
            if arr[i] == arr[j]:
                continue
            else:
                max_dis = max(max_dis, (j-i))

        max_distances.append(max_dis)

    return max(max_distances)

def max_distance_bet_unequal_elements_optimal(arr, n):
    # If first and last elements are unequal then they are max dist apart
    if arr[0] != arr[n-1]:
        return n-1

    # Fix first element as one of the element and start traversing from end to find unequal element index
    i = n-1
    while i > 0:
        if arr[i] != arr[0]:
            break
        else:
            i -= 1

    print(i)
    first_elem_dist = -1 if i == 0 else i
    print(first_elem_dist)


    # Fix last element as one of the element and start travesing from start
    i = 0
    while i < n-1:
        if arr[i] != arr[n-1]:
            break
        else:
            i += 1

    print(i)
    last_elem_dist = -1 if i == n-1 else (n-1-i)
    print(last_elem_dist)

    max_dist = max(first_elem_dist, last_elem_dist)

    return max_dist




def main():
    arr1 =  [3, 3, 2, 1, 2, 1, 3]

    print("Using Brute force method: {}".format(max_distance_bet_unequal_elements_loops(arr1, len(arr1))))
    print("Using Optimal method: {}".format(max_distance_bet_unequal_elements_optimal(arr1, len(arr1))))

    arr2 = [3,3,1,3,3]

    print("Using Brute force method: {}".format(max_distance_bet_unequal_elements_loops(arr2, len(arr2))))
    print("Using Optimal method : {}".format(max_distance_bet_unequal_elements_optimal(arr2, len(arr2))))

if __name__ == '__main__':
    main()
