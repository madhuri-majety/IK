"""
Given a list of strings, return a list with grouping of anagrams

input = ['cat', 'tac', 'dog', atc', 'god', 'fun', 'ogd', 'odg']
output = [['cat', 'tac', 'atc'], ['dog', 'god', 'ogd', 'odg'], ['fun']]

"""

def are_anagram_xor(str1, str2):
    if len(str1) != len(str2):
        return False

    value = 0

    for i in range(len(str1)):
        value = value ^ ord(str1[i])
        value = value ^ ord(str2[i])

    return value == 0

# Driver code
str1 = "geeksforgeeks";
str2 = "forgeeksgeeks";
if(are_anagram_xor(str1, str2)):
    print("The two strings are anagram of each other");
else:
    print("The two strings are not anagram of each other");
