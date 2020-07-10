"""
Company: Juniper Networks



Given an array with integer elements in small range, sort the array. We need to write a non-comparison based sorting algorithm with following assumptions about input.

    All the entries in the array are integers.
    The difference between the maximum value and the minimum value in the array is less than or equal to 10^6.

https://www.geeksforgeeks.org/sorting-without-comparison-of-elements/

Solution:
Since the range of elements are small, we can create a large count array that can fit all these numbers.
******** We use array elements as indices in large count array and print every non-zero index with the
count times(if array have duplicate numbers)  *******

To make this stable, we need to use **** Counting Sort *****
"""

MIN = 0
MAX = 100

def sort_without_comparision(arr, n):
    """
    Time Complexity = O(n + (Max-Min))
    Space Complexity = O(MAX - MIN + 1)
    Stable: NO
    :param arr:
    :param n:
    :return:
    """
    count_arr_no_elems = MAX - MIN + 1
    sorted = []

    # Initialize the count array with 0's
    count_arr = [0] * count_arr_no_elems

    # Populate the Count array with count of elements in given array
    for num in arr:
        count_arr[num] += 1

    for i in range(count_arr_no_elems):
        for j in range(count_arr[i]):
            sorted.append(i)

    return sorted

if __name__ == '__main__':
    arr = [10, 10, 1, 4, 4, 100, 0]
    print(sort_without_comparision(arr, len(arr)))


