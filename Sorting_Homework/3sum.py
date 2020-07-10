"""
3 Sum - Given an array of N integers, find all triplets that sum to 0.

Triplets may or may not be consecutive numbers
The array can include duplicates
Array is not necessarily sorted
https://www.programcreek.com/2012/12/leetcode-3sum/
https://www.geeksforgeeks.org/find-number-of-triangles-possible/
Time Complexity = O(n^2)
Space Complexity = O(1)
"""

def three_sum(arr):
    # Sort the array so that, duplicates can be avoided
    arr, result, i = sorted(arr), [], 0
    while i < len(arr)-2:
        if i == 0 or arr[i] != arr[i-1]:
            j, k = i+1, len(arr)-1
            while j < k:
                if arr[i] + arr[j] + arr[k] < 0:
                    j += 1
                elif arr[i] + arr[j] + arr[k] > 0:
                    k -= 1
                else:
                    result.append([arr[i], arr[j], arr[k]])
                    #result.append(",".join((str(arr[i]), str(arr[j]), str(arr[k]))))
                    j, k = j+1, k-1
                    while j < k and arr[j] == arr[j-1]:
                        j += 1
                    while j < k and arr[k] == arr[k+1]:
                        k -= 1
        i += 1

    return result

def main():
    s = [-1, 0, 1, 2, -1, -4]

    print("Printing 3sum values:", three_sum(s))

if __name__ == '__main__':
    main()
