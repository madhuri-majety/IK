"""
In an unsorted array, find the minimum distance between two numbers x and y
Array might contain duplicates.
https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/


"""
import sys
INT_MAX = sys.maxint

def minimum_distance_two_loops(arr, x, y):
    """
    In this method, two loops are used outer loop and inner loop.
    The outer loop picks the elements one by one
    The inner loop picks all the elements after the element picked by the outer loop.
    If elements picked are equal to x or y then if needed update the min distance

    TC - O(N^2) due to two loops
    SC - O(1)
    :param arr:
    :param x:
    :param y:
    :return:
    """
    min_dist = INT_MAX

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if ((arr[i] == x and arr[j] == y) or (arr[i] == y and arr[j] == x)) and abs(i-j) < min_dist:
                min_dist = abs(i-j)

    return min_dist


def minimum_distance_optimal(arr, x, y):
    """
    In the is method,
    - Traverse the array from left to right and see if element matches to x or y. If yes stop the loop and store the index
      in a variable 'prev'
    - Now continue traversing the array from where previous step stopped and check if element matches to x or y
        - If matches and element is same as element in prev, update prev index
        - If element doesnot match with element in prev and distance is less the min distance then update the min distance

    TC = O(n)
    SC = O(1)
    :param arr:
    :param x:
    :param y:
    :return:
    """
    min_dist = sys.maxint

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            prev = i
            break

    while i < len(arr):
        if arr[i] == x or arr[i] == y:
            if arr[prev] != arr[i] and (i-prev) < min_dist:
                min_dist = (i-prev)
                prev = i
            else:
                prev = i

        i += 1

    return min_dist




def main():
    arr = [5, 3, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    x = 3
    y = 6

    print("Using Two Loops: ", minimum_distance_two_loops(arr, x, y))
    print("**********************")
    print("Using Optimal Solution:", minimum_distance_optimal(arr, x, y))

if __name__ == '__main__':
    main()
