"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Notes:
    This is same string pattern matching problem. Two ways to solve the problem
        - Naive pattern matching (O(N^2))
        - KMP algorithm O(N)
See strings problems for KMP algorithm
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    break

            else:
                return i

        return -1

def main():
    sol = Solution()
    print(sol.strStr("hello", "ll"))
    print(sol.strStr("aaaaaa", "ll"))
    print(sol.strStr("a", ""))

if __name__ == '__main__':
    main()




