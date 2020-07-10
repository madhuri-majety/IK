"""
Given a string, print the longest substring without repeating characters.
For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”,
 with length 6. For “BBBB” the longest substring is “B”, with length 1.
 The desired time complexity is O(n) where n is the length of the string.

https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/

Approach:
Brute force : Generate all substrings, find all substrings with unique chars and find the longest substring
Optimal: Sliding Window Mechanism (Always O(N))
- In all sliding window problems, maintain a window that satisfies the criteria, once the condition is violated then
calculate max at the point and update the result variables like maxlength and start pointer so we can construct the
substring from it at the end. At the point of violation, we move the start of the window to satisfy the criteria again
and countinue expanding the window (in other words continue to traverse the sequence)

In this problem we maintain a window that satisfies the criteria and when the criteria is violated we calculate the
max length and start pointer that can help in constructing the substring.
When the criteria is violated we move out window to the next position in the string. For this we need the previous
index positions so auxillary data structure to use here is hash with key as character and value as the previous index
when same character is encountered we move our window to the next position of the previous occurence of the character.
"""

def longest_unique_substring(str):
    n = len(str)

    if n <= 1:
        print(n)
        return

    st = 0      # Starting point of current substring

    max_length = 0  # Max length of substring found so far

    start = 0   # Start of the max substring found so far

    i = 0   # Iterator for the string

    pos_map = {}   # Map to maintain the positions of the characters
    pos_map[ord(str[i])] = i     #Store the first character pos in pos_map

    for i in range(1, n):
        if ord(str[i]) not in pos_map:
            pos_map[ord(str[i])] = i

        else:
            if pos_map[ord(str[i])] >= st:
                cur_len = i - st
                if max_length < cur_len:
                    max_length = cur_len
                    start = st


                # Next substring will start after the last
                # occurrence of current character to avoid
                # its repetition.
                st = pos_map[ord(str[i])] + 1

            # Update the last occurrence of the character
            pos_map[ord(str[i])] = i

    print(i)
    if max_length < i - st + 1:
        max_length = i - st + 1     # *** Don't forget to add 1 as the slicing operation need to have one extra
        start = st

    print("Substring: {}, Length: {}".format(str[start:max_length+start], len(str[start:max_length+start])))

def main():
    longest_unique_substring("abcabc")
    longest_unique_substring("abcdabc")
    longest_unique_substring("abcabcde")
    longest_unique_substring("GEEKSFORGEEKS")
    longest_unique_substring("Asdfcbnsfdwer")
    longest_unique_substring("abba")
    longest_unique_substring("pwwkew")
    longest_unique_substring("aaaaaa")
    longest_unique_substring("a b c")
    longest_unique_substring("aab")

if __name__ == '__main__':
    main()

