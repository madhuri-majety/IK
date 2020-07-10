#! /usr/bin/python3

def ispalindrome_rec(s):
    if len(s) <= 1:
        return True
    else:
        return((s[0]==s[-1]) and ispalindrome(s[1:-1]))

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

def ispalindrome(s):
    """
    One line to check if the string is a palindrome or not
    :param s: string
    :return: boolean
    """
    return s == s[::-1]

str = input("Input the string to check for Palindrome:")
#str = "".join(str.split())
#str = str.replace(" ","")
if(ispalindrome_rec(str)):
    print("{} is palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))

if(ispalindrome_rec_optimized(str, 0, len(str)-1)):
    print("{} is palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))

