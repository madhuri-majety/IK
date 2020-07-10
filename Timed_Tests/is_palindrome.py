"""
Function to recursively check, if string s in range start to end (both inclusive), is a valid
palindrome or not.
"""

def ispalindrome_rec_optimized(s, start, end):
    """
    end index is non inclusive
    :param s:
    :param st:
    :param en:
    :return:
    """
    if start == end:
        return True

    if end-start == 1:
        return True

    if not s[start].isalnum():
        start = start + 1

    if not s[end].isalnum():
        end = end - 1

    if s[start] != s[end]:
        return False

    return ispalindrome_rec_optimized(s, start+1, end-1)

str = input("Input the string to check for Palindrome:")

if(ispalindrome_rec_optimized(str, 0, len(str)-1)):
    print("{} is palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))