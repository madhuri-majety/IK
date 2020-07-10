"""
Shortest substring that controls a given set of characters
input = "Helloworld"
set = {l,r,w}

Output: 'worl'

https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

"""
import sys

MAXINT = sys.maxsize

def shortest_substr_has_set_of_chars_bruteforce(s, char_set):
    """
    In this brute force method, we will compute all possible substrings
    Then find all substrings that has the char_set and find the min length
    substring that has all characters in char_set
    :param s:
    :param char_set:
    :return:
    """
    ## Step 1: Find all the possible substrings

    substrs = []
    min = MAXINT
    shortest_substring = ''
    size = len(s)

    for i in range(size):
        for j in range(i+1, size+1):
            inter = []
            for k in range(i, j):
                inter.append(s[k])
            substrs.append("".join(inter))

    print("All possible substrings are : {}".format(substrs))

    ## Step 2: If a substring contains char_set then compute the lenght
    ## of substring and compare with exisitng min value and adjust min

    for substr in substrs:
        if (set(substr) >= set(char_set)) and len(substr) < min:
            print(substr)
            min = len(substr)
            shortest_substring = substr

    print("Shortest substring is :{}".format(shortest_substring))


def shortest_substr_has_set_of_chars_optimal(s, char_set):
    """
    First check if the length of string is less that the length of the given pattern or char set,
    if yes then no such window can exist
    Store the occurrences of characters of the given pattern in a hash_pat dict
    Start matching the characters of pattern with the characters of the string i.e., increment count if a
    character matches
    Check if count == length of pattern/control set this means window is found.
    If such window found, try to minimize it by removing extra characters from the beginning of the current window.
    Update min_length
    Print minimum length window.
    TC = O(N)
    SC = O(N)
    :return:
    https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
    """
    len_s = len(s)
    len_charset = len(char_set)
    #print(char_set)

    if len_s < len_charset:
        print("No such window exists")
        return

    hash_charset = [0] * 256
    hash_s = [0] * 256

    for i in range(len_charset):
        #print("Updating hash_charset")
        hash_charset[ord(char_set[i])] += 1

    print("Debug: Hash of char_set is : {}".format(hash_charset))

    start, start_index, min_len = 0, -1, MAXINT

    # Variable that keep tracks of count of char set occurrences in a string
    count = 0

    for j in range(len_s):
        # Count occurrence of characters of string
        hash_s[ord(s[j])] += 1

        # If strings character matches with character in char_set then
        # increment the count. But increment only if that character is
        # not seen before
        if (hash_charset[ord(s[j])] != 0 and
            hash_s[ord(s[j])] <= hash_charset[ord(s[j])]):
            count += 1
        #print("String index is {}".format(j))
        #print("Count is {}".format(count))

        # If count matches the number of characters in char_set
        if count == len_charset:
            #print("Entered into Contraction Phase")
            # We found our window that has all characters in char_set
            # So try to minimize the window i.e. check if any character
            # is occurring more number of times than its occurrence in
            # char_set, if yes then remove it from the starting and
            # also remove useless characters
            while (hash_charset[ord(s[start])] == 0 or
                   hash_s[ord(s[start])] > hash_charset[ord(s[start])]):
                if (hash_s[ord(s[start])]) > hash_charset[ord(s[start])]:
                    hash_s[ord(s[start])] -= 1
                start = start + 1

            # Update window size
            window_len = j - start + 1
            if window_len < min_len:
                min_len = window_len
                start_index = start
                #print("Current Min length & start_index: {}, {}".format(min_len, start_index))


    # If no window found then return
    if start_index == -1:
        print("No substring found")
        return

    print(s[start_index : start_index + min_len])


def shortest_substr_has_set_of_chars_optimal_hash(s, char_set):
    hash_s = {}
    hash_charset = {}
    start = 0
    start_index = -1
    min_len = sys.maxsize
    count = 0


    for i in char_set:
        hash_charset[i] = hash_charset.get(i, 0) + 1

    print(hash_charset)

    for j in range(len(s)):
        hash_s[s[j]] = hash_s.get(s[j], 0) + 1

        if s[j] in hash_charset and hash_s[s[j]] <= hash_charset[s[j]]:
            count = count + 1
        #print(count)
        if count == len(char_set):
            #print(hash_s, hash_charset)
            while s[start] not in hash_charset or hash_s[s[start]] > hash_charset[s[start]]:
                if hash_s[s[start]] > hash_charset.get(s[start], 0):
                    hash_s[s[start]] = hash_s.get(s[start])-1
                start = start + 1

            window_len = j - start + 1
            if window_len < min_len:
                min_len = window_len
                start_index = start

    if start_index == -1:
        print("No Substring found")
        return

    print(s[start_index: start_index+min_len])


def main():
    s = "helloworld"
    char_set = {'l', 'w', 'r'}

    print("********** Using Brute Force ************")
    shortest_substr_has_set_of_chars_bruteforce(s, char_set)

    print("********* Using Optimal Solution ***********")
    shortest_substr_has_set_of_chars_optimal(s, list(char_set))


    print("********* Using Optimal Solution using hash DS ***********")
    shortest_substr_has_set_of_chars_optimal_hash(s, list(char_set))
    shortest_substr_has_set_of_chars_optimal_hash("ADOBECODEBANC", list("ABC"))

if __name__ == '__main__':
    main()
