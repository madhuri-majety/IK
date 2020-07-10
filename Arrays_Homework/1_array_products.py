"""
Problem Statement:

Given an array of numbers nums of size n, find an array of numbers products of size n,
such that products[i] is the product of all numbers nums[j], where j!=i.

Input Format:
There is only one argument: nums, denoting input array

Output Format:
Return an array of numbers products, denoting the required product array

Constraints:

You can't use division anywhere in solution
2 <= n <= 100000
-2147483648 <= nums[i] <= 2147483647, i=1,2,3,...,n
-2147483648 <= products[i] <= 2147483647, i=1,2,3,...,n

Notes:
Usage of resultant products array will not be considered as extra space used.
Without using division is the key constraint to remember.


* *********************** PROBLEM DESCRIPTION ***************************
 * Given an array of numbers, nums, return an array of numbers products, where products[i]is the product of all nums[j],
 * j != i.
 * <p>
 * Input : [1, 2, 3, 4, 5]
 * Output: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
 * = [120, 60, 40, 30, 24]
 * You must do this in O(N) time, and constant space, without using division. Usage of products array is not considered
 * extra space.
 * <p>
 * Without using division is the key constraint to remember.

**************************************************
Given an array of numbers A of size N, find and print array of numbers P of size N, where P[i] is the product of all
numbers A[j], where j!=i.

A naive approach would be, to find ith element of output array(i.e. P[i]), iterate over an entire input array A to
get the product of all elements A[j], such that j!=i.

Time Complexity: O(N*N)
Auxiliary Space Used: O(1)

An optimal approach would be as follows:
Notice that for P[i], product of all input array elements other than ith element is nothing but
                       (product of all elements A[j], 0<=j<=(i-1)) * (product of all elements A[j], (i+1)<=j<=(N-1))
                     = (A[0]*A[1]*...*A[i-1]) * (A[i+1]*A[i+2]*...*A[N-1])

So, iterate input array A twice to fill output array P, once for updating P[i] with (A[0]*A[1]*...*A[i-1]), and next
one for updating P[i] with (A[i+1]*A[i+2]*...*A[N-1]).
Please see the commented code for detailed implementation of optimal approach.

Time Complexity: O(N)
Auxiliary Space Used: O(1)

https://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div


"""

def product_array_brute_force(nums):
    product = [None]*len(nums)
    for i in range(len(nums)):
        product[i] = 1
        for j in range(len(nums)):
            if j != i:
                product[i] = product[i] * nums[j]

    return product

def product_array_optimal_time_only(nums):
    product_below = [None]*len(nums)
    product_above = [None] * len(nums)
    product = [None] * len(nums)

    left_to_right = 1
    for i in range(len(nums)):
        product_below[i] = left_to_right
        left_to_right *= nums[i]

    right_to_left = 1
    for j in range(len(nums)-1, -1, -1):
        product_above[j] = right_to_left
        right_to_left *= nums[j]

    for k in range(len(nums)):
        product[k] = product_below[k] * product_above[k]

    return product

def product_array_optimal_time_and_space(nums):
    product = [None]*len(nums)

    # First pass, from left to right update each index(i) with product up to i-1
    left = 1
    for i in range(len(nums)):
        product[i] = left
        left *= nums[i]

    # Second pass, from right to left update each index(i) with product from i+1 to N
    right = 1
    for j in range(len(nums)-1, -1, -1):
        product[j] *= right
        right *= nums[j]

    return product


def main():
    nums = [1,2,3,4,5]
    print("Printing product for nums: {}".format(product_array_brute_force(nums)))

    arr = [4,9,10]
    print("Printing product for arr: {}".format(product_array_optimal_time_only(arr)))

    arr2 = [4, 9, 10]
    print("Printing product for arr2: {}".format(product_array_optimal_time_and_space(arr2)))


if __name__ == '__main__':
    main()

