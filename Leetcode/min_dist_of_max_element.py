"""
You are given an array of n-elements with a basic condition that occurrence of greatest element is more than once.
You have to find the minimum distance between maximums. (n>=2).
Input : arr[] = {3, 5, 2, 3, 5, 3, 5}
Output : Minimum Distance = 2
Explanation : Greatest element is 5 and its index
are 1, 4 and 6. Resulting minimum distance of 2
from position 4 to 6.

Input : arr[] = {1, 1, 1, 1, 1, 1}
Output : Minimum Distance = 1
Explanation : Greatest element is 1 and its index
are 0, 1, 2, 3, 4 and 5. Resulting minimum distance
of 1.

"""

def min_dist_of_max_elemets(arr, n):
    max_elem = arr[0]
    min_dist = n
    index = 0

    for i in range(1, n):
        if arr[i] == max_elem:
            min_dist = min(min_dist, (i-index))
            index = i
        elif(arr[i] > max_elem):
                max_elem = arr[i]
                min_dist = n
                index = i
        else:
            continue

    return min_dist

arr = [6, 3, 1, 3, 6, 4, 6]
n = len(arr)
print("Minimum distance =", min_dist_of_max_elemets(arr, n))
