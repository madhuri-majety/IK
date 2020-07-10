"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

https://leetcode.com/problems/container-with-most-water/

Algorithm

The intuition behind this approach is that the area formed between the lines will always be limited by the height
of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines.
Further, we maintain a variable maxarea to store the maximum area obtained till now.
At every step, we find out the area formed between them, update maxarea and move the pointer
pointing to the shorter line towards the other end by one step.
"""

def max_area_two_pointer(height):
    left = 0
    right = len(height)-1
    maxarea = 0

    while left < right:
        maxarea = max(maxarea, min(height[left], height[right]) * (right-left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxarea

def main():
    input = [1,8,6,2,5,4,8,3,7]
    print(max_area_two_pointer(input))

if __name__ == '__main__':
    main()
