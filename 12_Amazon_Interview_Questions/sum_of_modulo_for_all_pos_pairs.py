"""
Given an array of integers A. calculate the sum of A[i] %A[j] for all possible i,j pair. return sum%(10^9+7) as an output solve this problem on o(n).
Example:
Input: arr[] = {1, 2, 3}
Output: 5
(1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2)

    (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5

Input: arr[] = {1, 2, 4, 4, 4}
Output: 10

*******   All possible pairs means all permutations   ******
"""

import itertools

def sum_of_modulo_all_permutations_pythonic(seq):
    permutations = list(itertools.permutations(seq))

    sum = 0

    for pair in permutations:
        mod = pair[0]%pair[1]
        sum += mod

    return sum%(10**9 + 7)

if __name__ == '__main__':
    print(sum_of_modulo_all_permutations_pythonic([1,2,3]))
    print(sum_of_modulo_all_permutations_pythonic([1,2,3,4]))
    print(sum_of_modulo_all_permutations_pythonic([4,3,2,1]))
