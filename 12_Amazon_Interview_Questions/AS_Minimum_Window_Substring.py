"""
Given a string S and a string T, find the minimum window in S which will contain
 all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T,
    return the empty string "".
    If there is such window, you are guaranteed that there will
    always be only one unique minimum window in S.
"""
import sys

class Solution(object):
    def min_window_substring(self, str, charset):
        hash_str = {}
        hash_charset = {}
        start = 0
        start_index = -1
        minlen = sys.maxsize
        count = 0

        for ch in charset:
            hash_charset[ch] = hash_charset.get(ch, 0) + 1

        print(hash_charset)

        for i in range(len(str)):
            hash_str[str[i]] = hash_str.get(str[i], 0) + 1

            if str[i] in hash_charset and hash_str[str[i]] <= hash_charset[str[i]]:
                count += 1
            print(count)
            if count == len(charset):
                # Start contracting the window
                while str[start] not in hash_charset or hash_str[str[start]] > hash_charset[str[start]]:
                    if hash_str[str[start]] > hash_charset.get(str[start], 0):
                        hash_str[str[start]] = hash_str.get(str[start])-1

                    start = start + 1

                win_len = i - start + 1
                if win_len < minlen:
                    minlen = win_len
                    start_index = start
                    print(start_index)

        print(start_index)
        if start_index == -1:
            return None

        return str[start_index: start_index+minlen]


def main():
    sol = Solution()

    print(sol.min_window_substring("ADOBECODEBANC", "ABC"))

if __name__ == '__main__':
    main()
