"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

Therefore, return the median sliding window as [1,-1,-1,3,5,6].

"""
def median_in_sliding_window_brute_force(arr, k):
    n = len(arr)

    if n*k == 0:
        return []

    if k == 1:
        return arr

    medians = []

    for i in range(n-k+1):
        window = sorted(arr[i:i+k])
        if k % 2 == 0:
            medians.append((window[k//2-1] + window[k//2])*0.5)
        else:
            medians.append(window[k//2])

    return medians

def median_in_sliding_window_two_heaps(arr, k):
    """
    https://leetcode.com/problems/sliding-window-median/solution/

    :param arr:
    :param k:
    :return:
    """

def main():
    print("Printing medians in a brute force way")
    print(median_in_sliding_window_brute_force([1, 3, -1, -3, 5, 3, 6, 7], 3))


if __name__ == '__main__':
    main()

