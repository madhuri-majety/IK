"""
Given a string, find the longest substring which is palindrome.
For example, if the given string is 'forgeeksskeegfor', the output should be 'geeksskeeg'.

https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
"""
import sys

def is_palindrome(str):
    return (str == str[::-1])

def longest_palindromic_substring_bruteforce(str,n):
    """
    In this brute force solution we generate all possible substrings and check each substring and compare
    if it is a palindrome and if it is return the longest substring
    TC = O(N^3)
    SC = O(1)
    :param str:
    :return:
    """
    max_length = -sys.maxint
    longest_substring = ""
    for i in range(n):
        for j in range(i+1, n+1):
            temp = []
            for k in range(i, j):
                temp.append(str[k])

            substr = "".join(temp)
            if is_palindrome(substr) and max_length < len(substr):
                max_length = len(substr)
                longest_substring = substr


    print(longest_substring)


def longest_palindromic_substring_optimal(str, n):
    """
    * Imagine every element is the mid of the palindrome and expand from there and see if it is a palindrome or not
    * Idea is to generate all even length and odd length palindromes and keep track of longest palindromic substring
    * Way to generate odd length palindromes
        * Fix a center and expand in both directions  for longer palindrome
    * Way to generate even length palindromes
        * Fix two centers (end of first half of string and starting of second half of string) and expand in both directions


    Time Complexity = O(N * (N/2 + N/2)) == O(N^2)
    Space Complexity = O(1)
    :param str:
    :param n:
    :return:
    """
    max_length = 1
    start = 0

    for i in range(n):
        # Find even length palindrome with center as i-1 and i
        low = i-1
        high = i

        while(low >= 0 and high < n and str[low] == str[high]):
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

        # Find longest odd length palindrome with center as i
        low = i - 1
        high = i + 1
        while(low >= 0 and high <n and str[low] == str[high]):
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

    longest_substring = str[start : start+max_length]

    print(longest_substring)


def testcases():
    str = "forgeeksskeegfor"
    print("******** Using Bruteforce Method *********")
    longest_palindromic_substring_bruteforce(str, len(str))

    print("******** Using Optimal way **************")
    longest_palindromic_substring_optimal(str, len(str))

    str1 = "ammadamabab"
    longest_palindromic_substring_optimal(str1, len(str1))


if __name__ == '__main__':
    testcases()
