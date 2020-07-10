"""

K’th Non-repeating Character

Given a string and a number k, find the k’th non-repeating character in the string. Consider a large input string
 with lacs of characters and a small character set. How to find the character by only doing only one traversal
 of input string?

Examples:

Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.

https://www.geeksforgeeks.org/kth-non-repeating-character/

Approach:
Idea is to use two auxillary arrays of size 256 (assuming a character is 8 bits long).
The two arrays are:
    - Count array which maitains the count of character
    - Index array which stores a valid index for non-repeating character and invalid index for repeating characters.
Initialize count array to all 0's
Initialize index array to invalid values (lets say size of the string as size is 1 greater than a valid index)
Traverse through the string and update the count of the character.
If count == 1, then update the index array with its index
If count > 1, then update it back to invalid index value.

now index array as values with valid string indices and in valid indices.
Sort the index array to find the kth non-repeating character. If index k is invalid index then return -1 else return the
charcter at valid index.
"""

MAX_CHARS = 256

def find_kth_non_repeating_char(str, k):
    n = len(str)
    count = [0] * MAX_CHARS
    index = [n] * MAX_CHARS

    for i in range(n):
        count[ord(str[i])] += 1

        if count[ord(str[i])] == 1:
            index[ord(str[i])] = i

        else:
            index[ord(str[i])] = n

    index.sort()

    if index[k-1] != n:
        print(str[index[k-1]])
    else:
        print(-1)

def main():
    find_kth_non_repeating_char("geeksforgeeks", 3)
    find_kth_non_repeating_char("aaaaaa", 2)

if __name__ == '__main__':
    main()
