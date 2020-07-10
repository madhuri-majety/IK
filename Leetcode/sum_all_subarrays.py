"""
Given an integer array of size n, find sum of all sub-arrays of given array

arr = [1,2,3]
output = 20
subarrays = [[1],[1,2],[1,2,3], [2], [2,3], [3]] = 6 subarrays (2^n)

https://www.geeksforgeeks.org/sum-of-all-subarrays/

"""

def sum_all_subarrays_loops(arr,n):
    result = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                result += arr[k]

    return result

def sum_all_subarrays_formula(arr,n):
    """
    arr = [1,2,3]
    subarrays = [1], [1,2], [1,2,3], [2], [2,3], [3]

    If looked at the pattern the arr[0] appears 3 times, arr[1] appears 4 times and arr[2] appears 3 times.

    Every element arr[i] appears in two types of subarrays
    1. Element arr[i] as the starting of the array => (n-i) times
    2. Element arr[i] which is not first element => (n-i)*i times

    So each element appears (n-i) + (n-i)*i ==> (n-1)*(i+1)
    So each element appears = arr[i]*(n-i)*(i+1)    ****************************
    :param arr:
    :param n:
    :return:
    """
    sum = 0
    for i in range(n):
        sum += arr[i]*(n-i)*(i+1)

    return sum


def main():
    arr = [1,2,3,4,6,7,8,9]
    print(sum_all_subarrays_loops(arr, len(arr)))
    print("**************************************")
    print(sum_all_subarrays_formula(arr, len(arr)))

if __name__ == '__main__':
    main()

