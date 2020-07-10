"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

"""


class Solution(object):
    def __init__(self):
        self.hash = {2: 'abc',
                     3: 'def',
                     4: 'ghi',
                     5: 'jkl',
                     6: 'mno',
                     7: 'pqrs',
                     8: 'tuv',
                     9: 'wxyz'}

    def letterCombinationsDFS(self, digits, idx, temp, res, n):
        # Base case
        if idx == n:
            res.append("".join(temp))
            return

        # Reccurence Relation
        for i in range(len(self.hash[digits[idx]])):
            temp.append(self.hash[digits[idx]][i])
            self.letterCombinationsDFS(digits, idx+1, temp, res, n)
            temp.pop()

        return res

    def letterCombinations(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        digits = list(s)
        nums = []
        for num in digits:
            if int(num) in self.hash.keys():
                nums.append(int(num))

        return self.letterCombinationsDFS(nums, 0, [], [], len(nums))
