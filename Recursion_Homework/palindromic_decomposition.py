"""
A palindromic decomposition of string S is a decomposition of the string into substrings,
such that all of those substrings are valid palindromes.

Input : abracadabra

output =
[
a|b|r|a|c|a|d|a|b|r|a|
a|b|r|aca|d|a|b|r|a|
a|b|r|a|c|ada|b|r|a|
]
"""
def isPali(input):
    return input[::-1] == input

def partition_rec(result, sofar, s, prefix_idx):
    if start == len(s):
        result.append(("|".join(sofar))+'|')
        print("Printing Result: {}\n".format(result))
    for j in range(start,len(s)):
        print("\n\n**** For Prefix Index as {}".format(j))
        cur = s[start:j+1]
        if isPali(cur):
            sofar.append(cur)
            print("Printing sofar after append:", sofar)
            partition_rec(result, sofar, s, j+1)
            sofar.pop()
            print("Printing sofar after pop:", sofar)
        else:
            print("{} is not a Palindrome".format(cur))

def palindrome_decompostition(s, prefix_index, sofar, result):
    if prefix_index == len(s):
        result.append(("|".join(sofar) + '|'))
        print("Printing result after DFS: {}".format(result))
    else:
        print("Prefix at Index {}".format(prefix_index))
        for suffix in range(prefix_index+1, len(s)+1):
            print("\tSuffix : {}, Prefix : {}".format(suffix, prefix_index))
            cur_substring = s[prefix_index : suffix]
            print("\tCurrent Substring: {}".format(cur_substring))
            if isPali(cur_substring):
                # Store this palindromic prefix into sofar list
                sofar.append(cur_substring)
                print("\t\tSofar palindromic substrings are {}".format(sofar))

                # Prefix is chosen, Now Recurse on suffix as final string to decompose to find the palindromes
                palindrome_decompostition(s, suffix, sofar, result)
                print("\t\tReturned from Recursion with sofar as {}".format(sofar))

                # At the depth of execution tree pop the prefix
                sofar.pop()
                print("\t\tPrinting sofar after pop: {}".format(sofar))
            else:
                print("\tSubstring {} is not a Palindrome".format(cur_substring))



def decompose(s):
    result = []
    palindrome_decompostition(s, 0, [], result)
    return result


#print(decompose("abracadabra"))
print(decompose("ab"))
