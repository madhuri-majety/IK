"""
Pattern matching using KMP algorithm

https://www.youtube.com/watch?v=GTJr8OvyEVQ
"""

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # Create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * M

    # Index for pattern
    j = 0

    # Preprocess the pattern and compute lps array
    computeLPSArray(pat, M, lps)

    # Index for txt
    i = 0

    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index: {}".format(i-j))

        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0 ... j-1] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    # Length of previous longest prefix suffix
    j = 0

    # lps[0] is always 0
    lps[0] = 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]

            else:
                lps[i] = 0
                i += 1

def main():
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    KMPSearch(pat, txt)

if __name__ == '__main__':
    main()


