"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""
import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        closest = float('inf')   # Positive Infinity value
        nums.sort()
        tripple = 0

        while i < len(nums) - 2:
            j = i+1
            k = len(nums) - 1
            while j < k:
                tripple = nums[i]+nums[j]+nums[k]
                if tripple == target:
                    return target
                if abs(tripple-target) < abs(closest-target):
                    closest = tripple
                if tripple - target > 0:
                    k -= 1
                else:
                    j += 1

            i = i + 1

        return closest

def main():
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
    print(sol.threeSumClosest([1, 1, -1], 2))
    print(sol.threeSumClosest([1,1,1,0], -100))


if __name__ == '__main__':
    main()

