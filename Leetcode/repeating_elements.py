"""
You are given an array of n+2 elements. All elements of the array are in range 1 to n.
And all elements occur once except two numbers which occur twice. Find the two repeating numbers.
For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice.
So the output should be 4 2.
"""

from collections import Counter

class Solution(object):
    def print_repeating_using_hash_map(self, nums):
        """
        In this method we use hash map to store the value and its count.
        While updating the count check if count exceeds 1 and add to the resulting array
        TC = O(N)
        SC = O(N+k) K being the number of elements repeating
        :param nums:
        :return:
        """
        count_to_map = {}
        result  = []

        for i in range(len(nums)):
            count_to_map[nums[i]] = count_to_map.get(nums[i], 0) + 1
            if count_to_map[nums[i]] > 1:
                result.append(nums[i])

        print("print_repeating_using_hash_map(): {}".format(result))

    def print_repeating_elems_using_counter_mod(self, nums):
        """
        In this method we use counter module to map items to its count
        Iterate through the list and see it's value in dictionary is greater than 1 and
        append that to th result.
        TC = O(N)
        SC = O(N + K)  K being the number of elements repeating
        :param nums:
        :return:
        """
        c = Counter(nums)
        print("Debug: Printing Counter object  - {}".format(c))
        result = []
        for item in nums:
            if c[item] > 1:
                if item not in result:
                    result.append(item)

        print("print_repeating_elems_using_counter_mod(): {}".format(result))

    def print_repeating_elements_optimal(self, arr):
        """
        As the assumption is that the elements in the array are within the index range, we can use the following logic
        "If the elements are repeating, that means multiple indices will have same value. As the arr have elements that
        matches the range of elements, we can traverse the array get the value of index which in turn can be used as
        index to the same array. Marking the element as visited my turning that into negative and compare the abs value
        to comparisions will give us the element being repeated

        As we are not using extra space, this is the optimal solution
        TC - O(N)
        SC = O(1)

        :param nums:
        :return:
        """
        result = []
        for i in range(len(arr)):
            # **** Notice the double indexing below *******
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])] = -1 * arr[abs(arr[i])]
            else:
                result.append(abs(arr[i]))

        print("print_repeating_elements_optimal() : {}".format(result))






def main():
    arr = [4, 2, 4, 5, 2, 3, 1]

    sol = Solution()
    sol.print_repeating_using_hash_map(arr)
    sol.print_repeating_elems_using_counter_mod(arr)
    sol.print_repeating_elements_optimal(arr)

if __name__ == '__main__':
    main()






