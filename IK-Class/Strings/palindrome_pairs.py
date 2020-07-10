"""
Find the palindrome pairs from the given list
Input: {dog, race, cat, car, mad, am, god}
Output: {racecar, madam, doggod, goddog}
"""

def is_palindrome(str):
    return str == str[::-1]

def palindrome_pairs_brute_force(strlist):
    """
    In this brute force way find all the possible pairs and check if each pair is a palindrome or not
    Time Complexity = O(N^3) (N^2 loop and N for palindrome check)
    Space Complexity = O(K)
    :param strlist:
    :return:
    """
    result = []

    for i in range(len(strlist)):
        for j in range(len(strlist)):
            if i != j:
                temp = strlist[i] + strlist[j]
                if is_palindrome(temp):
                    result.append(temp)

    return result

def palindrome_pairs_optimal_hash(strlist):
    result = []
    result_indices = set()
    worddict = {}
    # Store reversed words in dictionary
    worddict = {word[::-1]:i for i, word in enumerate(strlist)}

    print("Debug: Reversed words dict - {}".format(worddict))

    for i, word in enumerate(strlist):
        m = len(word)
        for k in range(m+1):
            # For word in strlist, find all possible prefixes in the
            # reversed words dict and if prefix is found and
            # remaining of the word that is suffix is also a
            # palindrome then attach actual word and reverse of dict item and
            # same for checking suffix as well
            prefix = word[:k]
            suffix = word[k:]
            if prefix in worddict and is_palindrome(suffix):
                if i != worddict[prefix]:
                    result.append((word+prefix[::-1]))
                    result_indices.add((i, worddict[prefix]))
            if suffix in worddict and is_palindrome(prefix):
                if i != worddict[suffix]:
                    result.append(suffix[::-1]+word)
                    result_indices.add((worddict[suffix], i))

    return result, list(result_indices)

class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False
        self.index = -1

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word, index):
        curr_node = self.root

        for char in range(len(word)):
            index = self._char_to_index(word[char])

            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]

        curr_node.end_of_word = True
        curr_node.index = index

    def search(self, word):
        curr_node = self.root

        for char in range(len(word)):
            index = self._char_to_index(word[char])
            if not curr_node.children[index]:
                return (False, -1)
            curr_node = curr_node.children[index]

        return (curr_node.end_of_word, curr_node.index)

    def display_util(self, curr_node, sofar, level):
        # Base case: If the current node is end of word then print the word
        if curr_node.end_of_word:
            print("".join(sofar[:level]))

        # Recursive case:
        for i in range(26):
            if curr_node.children[i]:
                sofar.insert(level, chr(i + ord('a')))
                self.display_util(curr_node.children[i], sofar, level+1)


    def display(self):
        sofar = []
        level = 0
        self.display_util(self.root, sofar, level)

class PalindromePairs(object):
    def palindrome_pairs_trie(self, words):
        def is_palindrome(str):
            return str == str[::-1]

        reverse_trie = Trie()
        result = set()

        # Insert the reverse of words in the Trie
        for i, word in enumerate(words):
            reverse_trie.insert(word[::-1], i)

        print("Priniting Reverse Trie")
        reverse_trie.display()

        for i, word in enumerate(words):
            m = len(word)
            for k in range(m+1):
                prefix = word[:k]
                suffix = word[k:]
                word_found, trie_index = reverse_trie.search(prefix)
                sword_found, strie_index = reverse_trie.search(suffix)

                if word_found and is_palindrome(suffix) and trie_index != i:
                    result.add(word+prefix[::-1])

                if sword_found and is_palindrome(prefix) and strie_index != i:
                    result.add(suffix[::-1]+word)

        return list(result)


def main():
    strlist = ['dog', 'race', 'cat', 'car', 'mad', 'am', 'god']
    strlist2 = ["abcd","dcba","lls","s","sssll"]
    strlist3 = ["a", ""]
    print("****** Printing Palindrome pairs using Brute force")
    print(palindrome_pairs_brute_force(strlist))
    print("\n\n")
    print(" **** Printing palidrome pairs using hash method *****")
    print(palindrome_pairs_optimal_hash(strlist))

    print("\n\n\n")
    print("****** Printing Palindrome pairs using Tries")
    p = PalindromePairs()
    print(p.palindrome_pairs_trie(strlist2))

if __name__ == '__main__':
    main()
