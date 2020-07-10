"""
Write a program to Reverse the given string while preserving the position of spaces.

Examples:

Input  : "abc de"
Output : edc ba

Input : "intern at geeks"
Output : skeegt an retni

Input : "Help others"
Output : sreh topleH

https://www.geeksforgeeks.org/reverse-string-preserving-space-positions/

Algorithm:

Create a string to store result. Mark the space position of the given string in this string.
Insert the character from input string into the result string in reverse order.
while inserting the character check if the result string already contains a space at index 'j' or not.
If it contains, we copy the character to the next position.

"""

def reverse_string_preserve_space(txt):
    input_char_list = list(txt)
    result = [None]* len(input_char_list)

    for i in range(len(input_char_list)):
        if txt[i] == ' ':
            result[i] = ' '

    j = len(result)-1
    for i in range(len(input_char_list)):
        if txt[i] != ' ':
            if result[j] == ' ':
                j -= 1
            result[j] = txt[i]
            j -= 1

    print("".join(result))

def reverse_string_preserve_space_optimal(txt):
    """
    Avoided the first loop in the above method as we can directly copy the original string which will have
    spaces at right position and then overwrite the non-space characters with the reverse string.
    :param txt:
    :return:
    """
    input_char_list = list(txt)
    result = list(txt)

    j = len(result)-1
    for i in range(len(input_char_list)):
        if txt[i] != ' ':
            if result[j] == ' ':
                j -= 1
            result[j] = txt[i]
            j -= 1

    print("".join(result))



def main():
    print("****** Priniting in Brute force **********")
    reverse_string_preserve_space("internship at geeks for geeks")

    print("******* Printing in OPtimal way **********")
    reverse_string_preserve_space_optimal("internship at geeks for geeks")


if __name__ == '__main__':
    main()
