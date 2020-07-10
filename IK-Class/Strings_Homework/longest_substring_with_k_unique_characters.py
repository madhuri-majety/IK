"""
Find the longest substring with k unique characters in a given string
OR
Find the longest substring with atmost 2 distinct characters
https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/



"""

import sys

def longest_substring_with_k_unique_chars_brute_force(txt, k):
    """
    This is a brute force solution. Generate all possible substrings and keep track of longest
    substring with k unique characters
    Time Complexity = O(N^3)
    SC = O(1)
    :param txt:
    :param k:
    :return:
    """
    longest = -sys.maxint
    longest_substring = None

    for i in range(len(txt)):
        for j in range(i+1, len(txt)+1):
            res = []
            for m in range(i, j):
                res.append(txt[m])
            substring = "".join(res)
            if len(set(substring)) == k and len(substring) > longest:
                longest = len(substring)
                longest_substring = substring

    return longest_substring

def longest_substring_with_k_unique_chars_sliding_window_optimal(txt, k):
    """
    Using the sliding window mechanism.

    :param txt:
    :param k:
    :return:
    """
    n = len(txt)
    win_start = 0
    win_end = 0
    cnt_hash = {}
    window_size = 1
    max_window_start = 0

    for i in range(n):
        if txt[i] in cnt_hash:
            cnt_hash[txt[i]] = cnt_hash.get(txt[i]) + 1
        else:
            cnt_hash[txt[i]] = 1
        win_end += 1
        print(cnt_hash)

        if len(cnt_hash.keys()) == k:
            # *** window size is end-start only not end-start+1 because by the time we enter into this
            # if condition, end moved to next character already
            if win_end - win_start > window_size:
                max_window_start = win_start
                window_size = win_end - win_start

        while len(cnt_hash.keys()) > k :
            if cnt_hash[txt[win_start]] > 1:
                cnt_hash[txt[win_start]] = cnt_hash.get(txt[win_start])-1
            else:
                del cnt_hash[txt[win_start]]
            win_start += 1

    print("Before returning result {} {}".format(max_window_start, max_window_start+window_size))
    return txt[max_window_start : max_window_start+window_size]


def main():
    txt = "aabbcc"
    k = 3
    txt1 = "karappa"
    k1 = 3

    print("******* Printing using Brute Force *********")
    print(longest_substring_with_k_unique_chars_brute_force(txt, k))

    print("***** Printing using Sliding Window mechanism *****")
    print(longest_substring_with_k_unique_chars_sliding_window_optimal(txt, k))
    print("\n\n")
    print(longest_substring_with_k_unique_chars_sliding_window_optimal(txt1, k1))

if __name__ == '__main__':
    main()


