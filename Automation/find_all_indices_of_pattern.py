"""
Find all indices of a pattern in a string

***** In python strings, there is a built in method to find the first occurrence of pattern and last
occurrence of pattern in a given string. But there is no method to return all indices of the pattern
"""

def find_all_occurences_of_pattern(inp_str, pattern):
    result = []
    start_index = 0
    while True:
        index = inp_str.find(pattern, start_index)
        if index == -1:
            break
        else:
            result.append(index)
        start_index = index + 1

    return result

def pattern_matching_sliding_window(inp_str, pattern):
    result = []
    n = len(inp_str)
    m = len(pattern)

    for i in range(n-m+1):
        for j in range(m):
            if inp_str[i+j] != pattern[j]:
                break

        if j == m-1:
            result.append(i)

    return result

def main():
    inp = "Our business is our business, none of your business"
    pattern = "business"

    print("***** Printing Pattern matches using Pythonic way *****")
    print(find_all_occurences_of_pattern(inp, pattern))

    print("\n\n")
    print("***** Printing Pattern matches using sliding window mechanism *****")
    print(pattern_matching_sliding_window(inp, pattern))


if __name__ == '__main__':
    main()
