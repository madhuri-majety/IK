"""
Implement a regular expression matcher that supports following characters
"." matches any single characters
"*" zero or more of the preceeding elements
example:
def matcher( "abcbc","ab.bc" ) -> True
def matcher("abcbbc", "abcb*c") ->True
def matcher("abcc", abccb*") -> True
def matcher("abc","a*bc") -> True
def matcher("bc","a*bc") -> True
def matcher("aaaaaaaaabc", "a*bc") -> True
def matcher("aaaaaaabc","aa*bc") -> True
def matcher("aaaabcc","a*bc.") ->True
"""


def regex_matcher(regex, word):
    return regex_matcher_util(regex, 0, word, 0)


def regex_matcher_util(regex, i, word, j):
    # Base condition, if index of regex reached the end then that is the end of the matching process
    # If index of word exceeded the length of word then match is not found
    if i == len(regex):
        return j == len(word)

    # Recursive conditions

    # 1. If index of word is less the length word and character in word and regex matches
    # or the regex character is '.' then recursively call this function for next character match
    # in both regex and word
    if j != len(word) and (regex[i] == word[j] or (regex[i] == '.')):
        return regex_matcher_util(regex, i+1, word, j+1)

    # 2. If the regex character is '*' then we have to options either zero match in word or rest of the characters
    # match in word
    # Zero match means - identical to skipping that character in regex and move to next character
    # More match means - with same regex character *, advance the index in word to match as much as we can
    if regex[i] == '*':
        return (regex_matcher_util(regex, i+1, word, j)) or regex_matcher_util(regex, i, word, j+1)

    return False


def main():
    print regex_matcher("ab.bc", "abcbc")
    print regex_matcher("abcb*c", "abcbbc")
    print regex_matcher("abccb*", "abcc")
    print regex_matcher("a*bc", "abc")
    print regex_matcher("a*bc", "bc")
    print regex_matcher("a*bc", "aaaaaaaaabc")
    print regex_matcher("aa*bc", "aaaaaaabc")
    print regex_matcher("a*bc.", "aaaabcc")

if __name__ == '__main__':
    main()

