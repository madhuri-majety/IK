"""
Find a continous subset whos sum is zero.There can be duplicates
Input: [5,1,2,-3,6,-4,1]
output:
    -  Variation1: True or False based on existence
    -  Variation2: Return an array of interger res of size 2, where res[0] and res[1] denotes start and end index
    -  Variation3: Return actual subarray [1,2,-3] or [-3,6,-4,1] any one subset

What is the complexity, if we need to print all subsets?
This is variation of maximum subarray problem.
Sounds like a dequeue problem with sliding window.

A simple solution is to consider all subarrays one by one and check the sum of every subarray.
We can run two loops: the outer loop picks a starting point i and the
inner loop tries all subarrays starting from i (See this for implementation).
Time complexity of this method is O(n2).

Dict: We can also use hashing. The idea is to iterate through the array and for every element arr[i],
calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]).
 If the current sum has been seen before, then there is a zero sum array.
 Hashing is used to store the sum values, so that we can quickly store sum and find out whether the current sum is
 seen before or not.

 https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

"""

def find_subarray_sumzero_exists(arr):
    """
    arr = [1,4,-2,-2,5,-4,3]

    If we consider all prefix sums, we can notice that there is a subarray with 0 sum when:
        - Either a prefix sum repeats or
        - Prefix sum becomes 0

    Prefix sums for above array are:
    1,5,3,1,6,2,5

    Since prefix sum 1 repeats, we have a subarray

    :param arr:
    :return:
    """
    sum = 0
    hash = {}
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0:
            return True
        if sum not in hash:
            hash[sum] = i
        else:
            # Same sum is repeated,so there is subarray with sum zero
            return True
    print(hash)
    return False

def find_subarray_sumzero_inidices(arr):
    """
    If we consider all prefix sums, we can notice that there is a subarray with 0 sum when:
        - Either a prefix sum repeats or
        - Prefix sum becomes 0
    hash(sum_value_at_every_index) = [list of indices seen this sum value]

    arr = [5,1,2,-3,6,-4,1]
    i = 0, sum = 5, hash(5) = [0]
    i = 1, sum = 5+1 = 6, hash(6) = [1]
    i = 2, sum = 6+2 = 8, hash(8) = [2]
    i = 3, sum = 8-3 = 5, hash(5) = [0,3]  <---------
    i = 4, sum = 5+6 = 11, hash(11) = [4]
    i = 5, sum = 11-4 = 7, hash(7) = [5]
    i = 6, sum = 7+1 = 8, hash(8) = [2, 6] <---------

    hash(5) and hash(8) has more than two values, so there are two subarrays that add up tp sum zero

    so first subarray with sum zero = 0+1, 3 => [1,3]
    so second subarray with sume zero = 2+1, 6 => [3,6]

    :param arr:
    :return:
    """
    sum = 0
    hash = {}
    result = []
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0:
            hash[sum] = [i]
            result.append((0,i))
        elif sum not in hash:
            hash[sum] = [i]
        else:
            for each in hash[sum]:
                result.append((each+1, i))
            hash[sum].append(i)

    #print(result)
    if len(result):
        return result[0]
    else:
        return -1



def main():
    arr = [5,1,2,-3,6,-4,1]
    arr1 = [4,2,-1,-1,5]

    #print(find_subarray_sumzero_exists(arr))
    #print(find_subarray_sumzero_inidices(arr))

    print(find_subarray_sumzero_inidices(arr1))

    arr3 = [1,-1]
    print(find_subarray_sumzero_inidices(arr3))

    arr4 = [1]
    print(find_subarray_sumzero_inidices(arr4))

if __name__ == '__main__':
    main()


