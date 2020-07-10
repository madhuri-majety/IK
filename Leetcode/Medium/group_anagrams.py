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


https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict

def group_anagrams(strs):
    result = defaultdict(list)

    for str in strs:
        result[tuple(sorted(str))].append(str)

    return result.values()

def main():
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(input))

if __name__ == '__main__':
    main()

