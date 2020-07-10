"""
Compress a string with basic encoding , where you simply count the number of repeated characters.
Then also write a routine to decompress it.

eg:
Input: "AAAAA"
Output: 5A

Input: "BAAAB"
Output: "B3AB"

Input: "BABA"
Output: "BABA"


String can heave any character from basic ASCII set i.e it can now include numbers
Compressed length must not exceed original length. It can be same or less.
Algorithm:
a) Pick the first character from source string.
b) Append the picked character to the destination string.
c) Count the number of subsequent occurrences of the picked character and append the count to destination string.
d) Pick the next character and repeat steps b) c) and d) if end of string is NOT reached.

"""
from collections import OrderedDict

def run_length_encoding_orderdict(input):
    # Generate ordered dictionary for all lower case
    # alphabets
    ord_dict = OrderedDict.fromkeys(input, 0)

    # Now iterate through input string to calculate
    # frequency of each character,
    for ch in input:
        ord_dict[ch] += 1

    # Now iterate through dictionary to make output string
    output = ''
    for key, value in ord_dict.items():
        output = output + str(value) + key

    return output

def run_length_encoding(s):
    """
    Approach is 2 pointer solution. Keep one pointer on element to count
    and another pointer traverse the string and increments the count if
    same character or else append to result and reset the count and
    move the pointer.
    :param s:
    :return:
    """
    result = []
    cur_pointer = s[0]
    count = 1
    input = s+str('0')  # This is needed to avoid string out of index in for loop
    for this in range(1, len(input)):
        # If this character from input is same as current pointer character
        # then increment the count
        if input[this] == cur_pointer:
            count += 1
        # Else there are two cases to consider
        # Count == 1, current pointer character and this character are different, so append to result
        # Count > 1, then append count and the current character to result, them move the current pointer
        # to this character and reset the count to 1
        else:
            if count == 1:
                result.append(input[this-1])
            else:
                result.append(str(count))
                result.append(input[this-1])

            # Reset the count and move the current element to next element
            count = 1
            cur_pointer = input[this]

    rle_string = ''.join(c for c in result)
    #print(rle_string)
    if len(rle_string) <= len(input):
        return rle_string
    else:
        return input


if __name__ == '__main__':
    input = "AAAAA"
    input1 = "BAAAB"
    print(run_length_encoding(input1))
    print(run_length_encoding("aaabbccccaaabc"))




