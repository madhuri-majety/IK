"""
given = "batch"
output = [ b3h, ba2h, b2ch]
until 2
given = "nailed"
output = [n4d, na3d, n3ed, nai2d, n2led, na2ed]
https://www.careercup.com/question?id=5733696185303040
"""

def neuronyms(input_str, k):
    """
    Find all the strings with k length as number in between the characters
    Idea: Two loop solution
    - Outer loop defines the length of inner string to be replaced with number
    - Inner loop calucates the prefix and suffix with the above length maintained.
    :param input_str:
    :param k:
    :return:
    """
    n = len(input_str)
    result = []

    for length in range(k, n-k+1):
        for start in range (1, n - length):
            prefix = input_str[:start]
            suffix = input_str[(start+length):]
            res_str = prefix+str(length)+suffix
            result.append(res_str)

    return result

print(neuronyms("nailed", 2))
print(neuronyms("internalization", 6))
