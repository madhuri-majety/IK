"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

https://leetcode.com/problems/maximum-subarray/solution/

Look at divide & conquer approach in leetcode. Very interesting ****

"""
import sys

def max_sum_subarrays_bruteforce(arr):
    """
    Generate all subarrays and find sum of subarray and update global sum
    Time Complexity: O(N^3) for generating subarrays
    Space Complexity: O(1)
    :param arr:
    :return:
    """
    n = len(arr)

    max_sum = -sys.maxsize

    for i in range(n):
        for j in range(i+1, n+1):
            cur = sum(arr[i:j])
            if cur > max_sum:
                max_sum = cur

    print(max_sum)

def max_sum_subarray_greedy(arr):
    """
    Greedy Approach:
    Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
    Algorithm:
    The algorithm is general and straightforward:
        iterate over the array and update at each step the standard set for such problems:
            current element
            current local maximum sum (at this given point)
            global maximum sum seen so far.

    Time Complexity: O(N)
    Space Complexity: O(1)

    :param arr:
    :return:
    """
    cur_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        cur_sum = max(arr[i], cur_sum + arr[i])
        if max_sum < cur_sum:
            max_sum = cur_sum

    print(max_sum)

def max_sum_subarray_kadane_algo(nums):
    """
    Move along the array and modify the array itself.
    :param arr:
    :return:
    """
    n = len(nums)
    max_sum = nums[0]

    for i in range(1, n):
        if nums[i-1] > 0:
            nums[i] = nums[i-1] + nums[i]

        max_sum = max(max_sum, nums[i])

    print(max_sum)



def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr2 = [1,2,3,4,5,6,7]
    print("Printing using Brute Force")
    max_sum_subarrays_bruteforce(arr)
    max_sum_subarrays_bruteforce(arr2)

    print("Printing using Greedy approach")
    max_sum_subarray_greedy(arr)
    max_sum_subarray_greedy(arr2)

    print("Priniting using Kadane's algorithm")
    max_sum_subarray_kadane_algo(arr)
    max_sum_subarray_kadane_algo(arr2)


if __name__ == '__main__':
    main()
