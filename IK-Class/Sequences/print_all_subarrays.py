"""
Subarrays is a contiguous part of array. An array that is inside another array.
Input : [1,2,3,4]
Output = [1], [2], [3], [4], [1,2], [1,2,3], [1,2,3,4], [2,3], [2,3,4], [3,4]

No of subarrays = n(n+1)/2

subarrays <===> substrings

"""

def print_all_subarrays(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i+1, n+1):
            result.append(arr[i:j])

    print(result)

def main():
    arr = [1,2,3,4]
    print_all_subarrays(arr)

if __name__ == '__main__':
    main()
