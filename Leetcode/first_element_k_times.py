"""
First element occuring k times in an array
Input: {1, 7, 4, 3, 4, 8, 7},
k = 2
Output: 7
Both 7 and 4 occur 2 times.
But 7 is the first that occurs 2 times.
"""
from collections import OrderedDict

def first_element_k_times_two_loops(arr, k):
    """
    In this brute force method use two loops.
    Outer loop picks elements one by one
    Inner loop traverses rest of the array and counts the occurence of ith element and if end of inner loop the count
    exceeds k times then break the loop and return value of outer loop index

    TC - O(N^2)
    SC - O(1)
    :param arr:
    :param k:
    :return:
    """
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[j] == arr[i]:
                count += 1
        if count >= k:
            break
    return arr[i]

def first_element_k_times_optimal(arr, k):
    """
    In this optimal approach we can decrease the time complexity by using the hash map to store the occurences and
    return the first element with equal to greater than k

    TC - O(N)
    SC - O(N)
    :param arr:
    :param k:
    :return:
    """
    count_map = OrderedDict()
    key = -1
    for item in arr:
        count_map[item] = count_map.get(item,0) + 1

    print(count_map)

    for key in arr:
        if count_map[key] == k:
            return key
    return key


def main():
    arr = [3, 7, 7, 3, 3, 8, 7]
    k = 2

    arr2 = [4, 1, 6, 1, 6, 4]
    k2 = 1
    print("Using Brute force method:", first_element_k_times_two_loops(arr, k))

    print("Using  Optimal method:", first_element_k_times_optimal(arr2, k2))


if __name__ == '__main__':
    main()



