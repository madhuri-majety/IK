"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.


"""
from collections import defaultdict

class Solution(object):
    def group_anagrams(self, strs):
        result = defaultdict(list)

        for str in strs:
            result[tuple(sorted(str))].append(str)

        return result.values()

def main():
    sol = Solution()
    print(sol.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == '__main__':
    main()

