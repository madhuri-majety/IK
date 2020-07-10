"""
Given a string generate a longest unique substring

**** See the IK strings section for optimal way
"""

def find_longest_unique_substring_bruteforce(str):
    max_length = -1
    max_substring = None
    n = len(str)

    for i in range(n):
        for j in range(i+1, n+1):
            substr = str[i:j]
            unique = set(substr)

            if len(unique) == len(substr):
                if max_length < len(substr):
                    max_length = len(substr)
                    max_substring = substr

    print(max_substring)

def main():
    find_longest_unique_substring_bruteforce("abcabcd")
    find_longest_unique_substring_bruteforce("abcdabc")
    find_longest_unique_substring_bruteforce("Asdfcbnsfdwer")

if __name__ == '__main__':
    main()


