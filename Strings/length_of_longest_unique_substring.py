"""

Length of the longest substring without repeating characters

Given a string str, find the length of the longest substring without repeating characters.

    For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
    For “BBBB” the longest substring is “B”, with length 1.
    For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7

The desired time complexity is O(n) where n is the length of the string.

Brute Force:
Generate all possible substrings and check if it is the unique substring and calculate and lenght and update max_length
whenever it is found
Time complexity = O(N^3)

Optimal (Sliding Window mechanism)
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

Even if a string has only 1 character, that iself is the longest substring.
******* Maintain a visited array with index a ascii value of character and value in
that index is the last seen index value in given string  ****** (This is the key to this solution)
lets say visited = [-1] * 256
if given string = "abc"
visited[ord(a)] = 0 (0 is the index of a)
visited[ord(b)] = 1
visited[ord(c)] = 2

if lets say string is "abca"
when second a comes that is already been visited before, so we need to adjust the window to start from prev index of a
so the lenght gets updated to current index of string i - prev_index

"""
NO_OF_CHARS = 256

def length_of_longest_substring_sliding_window(str):
    """
    This is WRONG
    """
    n = len(str)

    if n == 0:
        return -1

    cur_len = 1
    max_len = 1
    start = 1
    i = 0

    # Initialize the index array
    visited = [-1] * NO_OF_CHARS

    # Update the index of first character
    visited[ord(str[i])] = i

    # Now iterate through rest of the characters and update the visited array
    for i in range(1, n):
        prev_index = visited[ord(str[i])]

        if prev_index == -1:
            # That means this character was not seen before, so increment the count
            cur_len += 1

        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        # Update the visited array with new index
        visited[ord(str[i])] = i

    # Compare the lenght again and update the max_length
    if cur_len > max_len:
        max_len = cur_len

    print(max_len)


def length_of_longest_substring_sliding_window_hash(s):
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
    print(len(substring))


def main():
    print("Using List Sliding window")
    length_of_longest_substring_sliding_window("abcabcd")
    length_of_longest_substring_sliding_window("abcdabd")
    length_of_longest_substring_sliding_window("Asdfcbnsfdwef")
    length_of_longest_substring_sliding_window("ABDEFGABEF")
    length_of_longest_substring_sliding_window("abba")

    print("\nUsing Hash Sliding Window")
    length_of_longest_substring_sliding_window_hash("abcabcd")
    length_of_longest_substring_sliding_window_hash("abcdabd")
    length_of_longest_substring_sliding_window_hash("Asdfcbnsfdwef")
    length_of_longest_substring_sliding_window_hash("ABDEFGABEF")
    length_of_longest_substring_sliding_window_hash("pwwkew")
    length_of_longest_substring_sliding_window_hash("abba")
    length_of_longest_substring_sliding_window_hash("aa")
    length_of_longest_substring_sliding_window_hash("aab")

if __name__ == '__main__':
    main()




