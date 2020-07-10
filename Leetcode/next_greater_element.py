"""
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
 Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.


Approach #3 Using Stack [Accepted]
In this approach, we make use of pre-processing first so as to make the results easily available later on.
We make use of a stack and a hashmap. map is used to store the result for every possible
number in nums in the form of (element, next\_greater\_element).
Now, we look at how to make entries in map.

We iterate over the nums array from the left to right.
We push every element nums[i] on the stack if it is less than the previous element on the top of the
stack (stack[top]). No entry is made in map for such nums[i]'s right now.
This happens because the nums[i]'s encountered so far are coming in a descending order.

If we encounter an element nums[i] such that nums[i] > stack[top],
we keep on popping all the elements from stack[top] until we encounter stack[k]
such that stack[k] ≤ nums[i]. For every element popped out of the stack stack[j],
we put the popped element along with its next greater number(result) into the hashmap,
in the form (stack[j], nums[i]) . Now, it is obvious that the next greater element
for all elements stack[j]stack[j], such that k < j ≤ top is nums[i](since this larger element caused
all the stack[j]'s to be popped out). We stop popping the elements at stack[k] because this
nums[i]nums[i] can't act as the next greater element for the next elements on the stack.

Thus, an element is popped out of the stack whenever a next greater element is found for it.
Thus, the elements remaining in the stack are the ones for which no next greater element exists in the
numsnums array. Thus, at the end of the iteration over numsnums, we pop the remaining elements from the stack
 nd put their entries in hash with a \text{-1}-1 as their corresponding results.

Then, we can simply iterate over the findNums array to find the corresponding results from map directly.

https://leetcode.com/problems/next-greater-element-i/solution/

"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        TC - O(m*n)
        Space Complexity - O(m)

        """
        res = [-1] * len(nums1)
        for i, item in enumerate(nums1):
            if item in nums2:
                idx = nums2.index(item)
                next = idx + 1
                while next <= len(nums2)-1:
                    if item < nums2[next]:
                        res[i] = nums2[next]
                        break
                    else:
                        next += 1
        return res

    def next_greater_elem_hash(self, nums1, nums2):
        """
        Time Complexity - O(m*n)
        Space Complexity - O(m+n)
        """
        elem_map = {}
        res = []
        for i in range(len(nums2)):
            j = i+1
            elem_map[nums2[i]] = -1
            while j <= len(nums2)-1:
                if nums2[i] < nums2[j]:
                    elem_map[nums2[i]] = nums2[j]
                    break
                else:
                    j = j + 1
        print("Hashmap of superset is {}".format(elem_map))

        for k in range(len(nums1)):
            res.append(elem_map[nums1[k]])

        return res


def main():
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(sol.nextGreaterElement(nums1, nums2))
    print("\n\n")
    nums3 = [1,3,5,2,4]
    nums4 = [6,5,4,3,2,1,7]
    print(sol.nextGreaterElement(nums3, nums4))
    print("\n*******************************\n")
    print(sol.next_greater_elem_hash(nums1, nums2))


if __name__ == '__main__':
    main()