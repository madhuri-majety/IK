"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the
array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Below Recursive solution runtime
Runtime: 20 ms, faster than 70.99% of Python online submissions for Plus One.
Memory Usage: 11.9 MB, less than 5.02% of Python online submissions for Plus One.

Iterative solution runtime
Runtime: 24 ms, faster than 39.38% of Python online submissions for Plus One.
Memory Usage: 11.7 MB, less than 62.15% of Python online submissions for Plus One.

"""


class Solution(object):
    def plusOne(self, digits):
        self.plusOneWrapper(digits, len(digits)-1)
        print(digits)
        #output = "".join(str(i) for i in digits)  # When joining integers convert to str and then join or else TypeError
        #print(output)

    def plusOneWrapper(self, digits, index):
        if index < 0:
            return
        if digits[index]+1 < 10:
            digits[index] = digits[index]+1
            return
        else:
            digits[index] = 0
            if index > 0:
                self.plusOneWrapper(digits, index-1)
            else:
                digits.insert(0,1)


class InteractiveSolution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1 < 10:
                digits[i] = digits[i]+1
                break
            else:
                if i > 0:
                    digits[i] = 0
                    continue
                else:
                    digits[i] = 0
                    digits.insert(0,1)
        print(digits)


def plus_one_leetcode(digits):
    if len(digits) == 1 and digits[0] ==9:
        return [1,0]
    elif digits[-1] != 9:
        return (digits[:-1]+[digits[-1]+1])
    else:
        return (self.plusOne(digits[:-1]) + [0])

def main():
    sol = Solution()
    input = [8,9,9,9]
    input2 = [8,9,9,9]
    sol.plusOne(input)
    sol1 = InteractiveSolution()
    sol1.plusOne(input2)


if __name__ == '__main__':
    main()
