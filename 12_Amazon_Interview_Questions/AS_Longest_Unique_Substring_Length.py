"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n <= 1:
            return n

        # Initialize max len to 0
        max_len = 0
        # Initialize a variable to mark the start of the current substring
        st = 0
        # Initialize a variable that marks the start of the max substring
        start = 0
        # Store first value of string in pos_map
        i = 0
        pos_hash = {}
        pos_hash[ord(s[i])] = i

        # Iterate through characters
        for i in range(1, n):
            if ord(s[i]) not in pos_hash:
                pos_hash[ord(s[i])] = i

            # Character is already in the position hash
            else:
                if pos_hash[ord(s[i])] >= st:
                    cur_len = i - st
                    if cur_len > max_len:
                        max_len = cur_len
                        start = st

                    # As current char is repeating, move the start of the current substring by 1
                    # from the prev occurrence of curr character
                    st = pos_hash[ord(s[i])] + 1

                # Update the pos hash with latest index
                pos_hash[ord(s[i])] = i

        if max_len < i - st + 1:
            max_len = i - st + 1
            start = st

        substring = s[start:max_len+start]
        return len(substring)

