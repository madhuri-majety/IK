"""
Given an array find the subset whose sum is equal to given target
Input: array, target
output: list of subsets

Approach:
Exclude first and until the end of the decision tree
start including if the sum is less than k
Base case: If reached end of the decision tree and total == k then print that subset and return
"""

def subset_sum_util(arr, idx, sum, res, res_idx, k):
    # Base case: If came to end of the decision tree and sum == k then print the result collected so far
    if idx == len(arr):
        # **** Dont check idx == len(arr) and sum ==k condition beacause that can cause RecursionError.
        if sum == k:
            print(res[:res_idx])
        else:
            return
    # Recurrence Relation: Exclusion first and then inclusion
    else:
        # Exclude recursion
        subset_sum_util(arr, idx+1, sum, res, res_idx, k)

        # Include last seen element to result if sum <= k
        res[res_idx] = arr[idx]
        # Inclusive recursion
        subset_sum_util(arr, idx+1, sum+arr[idx], res, res_idx+1, k)


def subset_sum(arr, k):
    result = [None] * len(arr)
    sum = 0

    return subset_sum_util(arr, 0, sum, result, 0, k)

def main():
    subset_sum([4, -3, 4, 8, 3], 0)

if __name__ == '__main__':
    main()
