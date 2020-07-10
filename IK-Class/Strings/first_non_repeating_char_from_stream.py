"""
Given a string, find the first non-repeating character in it.

For example, if the input string is “GeeksforGeeks”, then output should be ‘f’
and if input string is “GeeksQuiz”, then output should be ‘G’.

Solution 1:
Construct a dictionary with count and latest index of the occurrence of the character.
Iterate over the dictionary and find the lowest indexed non-repeating character

Solution 2:
Construct an ordered dictionary and populate the count.
Iterate over ordered dictionary and find the first key with count as 1
"""

from collections import OrderedDict

def find_first_non_repeating_char_hash(str):
    """
    Time Complexity to get first non-repeating char is O(N)
    Space Complexity is O(N)
    :param str:
    :return:
    """
    count_hash = {}
    min_idx = 100000        # Use sys.maxint
    for i, char in enumerate(str):
        if char not in count_hash:
            count_hash[char] = {}
            count_hash[char]['index'] = i
            count_hash[char]['count'] = 1
        else:
            count_hash[char]['index'] = i
            count_hash[char]['count'] = count_hash[char]['count'] + 1

    #print(count_hash)

    for key in count_hash.keys():
        if count_hash[key]['count'] == 1:
            if count_hash[key]['index'] < min_idx:
                min_idx = count_hash[key]['index']

    print(str[min_idx])

def find_first_non_repeating_char_ordered_dict(str):
    count_dict = OrderedDict()

    for i, char in enumerate(str):
        count_dict[char] = count_dict.get(char, 0) + 1

    #print(count_dict)

    for key in count_dict.keys():
        if count_dict[key] == 1:
            print(key)
            break




def main():
    find_first_non_repeating_char_hash("GeeksforGeeksm")
    find_first_non_repeating_char_hash("GeeksQuiz")

    print("\nUsing Ordered Dict")
    find_first_non_repeating_char_ordered_dict("GeeksforGeeksm")
    find_first_non_repeating_char_ordered_dict("GeeksQuiz")

if __name__ == '__main__':
    main()
