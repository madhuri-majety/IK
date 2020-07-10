"""
Subsequences are *NOT CONTIGUOUS*

Subsequences <==> Power sets

A subsequence is a sequence that can be derived from another sequence by zero or more elements,
without changing the order of the remaining elements.
For the same example, there are 15 sub-sequences. They are (1), (2), (3), (4), (1,2), (1,3),(1,4), (2,3),
(2,4), (3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4), (1,2,3,4). More generally, we can say that for a sequence of size n,
we can have (2n-1) non-empty sub-sequences in total.

A string example to differentiate: Consider strings “geeksforgeeks” and “gks”. “gks” is a subsequence of
“geeksforgeeks” but not a substring. “geeks” is both a subsequence and subarray. Every subarray is a subsequence.
More specifically, Subsequence is a generalization of substring.

How to generate all Subsequences?
We can use algorithm to generate power set for generation of all subsequences.

https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/

************ Subsequences <===> Powerset <===> Subsets  *************

"""

def print_all_subsequences(arr):
    """
    No of subsequences are equal to 2^n with empty subsequence which are equal to power set

    :param arr:
    :return:
    """
    result = []
    n = len(arr)
    two_power_n = pow(2, n)

    for i in range(two_power_n):
        temp = []
        for j in range(n):
            if i & 1 << j > 0:
                temp.append(arr[j])
        result.append(temp)

    print(result)


def main():
    arr = ['a','b','c']
    arr1 = [1,2,3,4]

    print_all_subsequences(arr)
    print_all_subsequences(arr1)

if __name__ == '__main__':
    main()

