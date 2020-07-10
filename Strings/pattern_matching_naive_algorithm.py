"""
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[],
char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
Naive Pattern Searching:
Slide the pattern over text one by one and check for a match. If a match is found,
then slides by 1 again to check for subsequent matches.

https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/

"""

def pattern_search_naive(string, pat):
    """
    There is a corner case which wont work here
    if string is not NULL and pat is NULL then this program will fail, following method uses for/else statement
    which fixes the issue
    :param string:
    :param pat:
    :return:
    """
    n = len(string)
    m = len(pat)
    result = []

    for i in range(n-m+1):

        # Fix the inner loop with the size of the pattern
        for j in range(0, m):
            if string[i+j] != pat[j]:
                break

        # If inner loop reaches the end of the pattern that means match is found
        if j == m-1:
            result.append(i)


    return result

def pattern_search_naive_CORRECT(string, pat):
    """
    There is a corner case which wont work here
    if string is not NULL and pat is NULL then this program will fail, following method uses for/else statement
    which fixes the issue
    :param string:
    :param pat:
    :return:
    """
    n = len(string)
    m = len(pat)
    result = []

    for i in range(n-m+1):

        # Fix the inner loop with the size of the pattern
        for j in range(m):
            if string[i+j] != pat[j]:
                break
        else:
            result.append(i)
            #return result

    return result


def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"

    print(pattern_search_naive_CORRECT(txt, pat))
    print(pattern_search_naive_CORRECT("a", ""))

if __name__ == '__main__':
    main()

