"""
Company: Juniper Networks

Remove a character from a string to make it a palindrome

Given a string, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

Examples:

Input  : str = “abcba”
Output : Yes
we can remove character ‘c’ to make string palindrome

Input  : str = “abcbea”
Output : Yes
we can remove character ‘e’ to make string palindrome

Input : str = “abecbea”
It is not possible to make this string palindrome
just by removing one character

https://www.geeksforgeeks.org/remove-character-string-make-palindrome/

Solution:
Traverse from both the ends of the string and stop where there is a mismatch
Two possibilities here:
Word with even characters:
    If even characters and if valid word, then either removing high or low pointer character
    Also checking if the left substring and right substrings around low or high pointers are palindromes or not

Word with odd characters:
    If odd characters and if valid word, then just removing low will be sufficient
    Also checking if the left substring and right substrings around low or high pointers are palindromes or not
"""


def is_palindrome(word1):
    if word1[::-1] == word1:
        return True
    return False


def remove_char_to_make_palindrome(str):
    low = 0
    high = len(str) - 1

    while low < high:
        if str[low] == str[high]:
            low += 1
            high -= 1

        else:
            # If came here then there is a mismatch then check two possibilities

            # Possibility #1: Exclude just character at index low
            print("Debug: {}, {}".format(str[:low], str[low+1:]))
            if is_palindrome(str[:low]+str[low+1:]):
                return low


            # Possibility #2: Exclude just character at index high
            print("Debug: {}, {}".format(str[:high], str[high+1:]))
            if is_palindrome(str[:high]+str[high+1:]):
                return high

            # If not return -1 marking it as not possible
            print("Not possible")
            return -1

    # Return status indicating that it is possible without even removing the character
    print("No need to remove anything")
    return -2


def main():
    print(remove_char_to_make_palindrome("abecbea"))
    print("****************************************")

    print(remove_char_to_make_palindrome("abeceba"))
    print("****************************************")

    print(remove_char_to_make_palindrome("abecba"))

if __name__ == '__main__':
    main()
