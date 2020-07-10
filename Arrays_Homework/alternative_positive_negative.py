"""
Given an array containing both +ve, -ve integers, return an array of alternating positive and negative integers
such that each of integers are in the same order as the input array
input = [2,3,-4,-9, -1, -7,1,-5,-6]
output =[2,-4, 3, -9,1,-1,-7,-5,-6]
implement this with out using additional space

Another optimal approach -
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

"""

def alternative_pos_neg_brute_force(arr):
    pos_arr, neg_arr = [], []
    st = arr[0]
    res = []

    for i in range(len(arr)):
        if arr[i] > 0:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])

    i,j = 0,0
    while i < len(pos_arr) and j < len(neg_arr):
        if st > 0:
            res.append(pos_arr[i])
            i += 1
            res.append(neg_arr[j])
            j += 1
        else:
            res.append(neg_arr[j])
            j += 1
            res.append(pos_arr[i])
            i += 1

    while i < len(pos_arr):
        res.append(pos_arr[i])
        i += 1

    while j < len(neg_arr):
        res.append(neg_arr[j])
        j += 1

    return res

def alternative_pos_neg_sub_optimal(arr):
    """
    TC - O(N^2)
    Space = constant
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        j = 0                   # j always starts from 0 as every while loop adjusts only 3 elements without checking back on previous values
        while j < len(arr)-2:   # As we are getting 2 inidices ahead of time we dont want to cross the boundary
            s = arr[j:j+3]
            s = [1 if x > 0 else -1 for x in s]

            if s[0] == s[1] and s[1] != s[2]:
                arr[j+1], arr[j+2] = arr[j+2], arr[j+1]

            j += 1

    return arr



def main():
    arr = [2,3,-4,-9,-1,-7,1,-5,-6]
    print("********* Brute Force ***************************")
    print(alternative_pos_neg_brute_force(arr))
    print(alternative_pos_neg_brute_force([1,2,3,4,4,5]))
    print(alternative_pos_neg_brute_force([-10,-9,-1,-4,-3]))
    print(alternative_pos_neg_brute_force([10, -9, 1, -4, 3]))
    print(alternative_pos_neg_brute_force([-10, 9, -1, 4, -3]))
    print(alternative_pos_neg_brute_force([1, 2, 3, -4, -1, 4]))

    print("********* Sub Optimal Solution **********************")
    print(alternative_pos_neg_sub_optimal(arr))
    print(alternative_pos_neg_sub_optimal([1, 2, 3, 4, 4, 5]))
    print(alternative_pos_neg_sub_optimal([-10, -9, -1, -4, -3]))
    print(alternative_pos_neg_sub_optimal([10, -9, 1, -4, 3]))
    print(alternative_pos_neg_sub_optimal([-10, 9, -1, 4, -3]))
    print(alternative_pos_neg_sub_optimal([1, 2, 3, -4, -1, 4]))



if __name__ == '__main__':
    main()
