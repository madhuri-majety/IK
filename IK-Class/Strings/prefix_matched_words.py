"""
Find the words starting with the prefix.
Input: {'Pizza Hut', 'Pieology', 'OPA', 'Pizza my heart', 'Pasta Place', 'Pizzeria'}
N strings with string length as M
Query: 'Pizza'
Query length = Q
Output: Pizza Hut, Pizza my heart ==> P results

"""

def prefix_matched_words_pythonic(strlist, prefix):
    result = []
    for word in strlist:
        if word.lower().startswith(prefix.lower()):
            result.append(word)

    return result


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = self.get_trie_node()

    def get_trie_node(self):
        return TrieNode()

    def _char_to_index(self, char):
        return (ord(char) - ord('a'))

    def add_word(self, word):
        top_node = self.root

        for i in range(len(word)):
            if word[i].isalpha():
                index = self._char_to_index(word[i])

                if top_node.children[index] is None:
                    top_node.children[index] = self.get_trie_node()
                top_node = top_node.children[index]

        top_node.is_end_of_word = True

    def display_util(self, curr_node, word, level, prefix=None):
        # Base case: If the curr_node is end of word then print the word until level
        if curr_node.is_end_of_word:
            if prefix:
                res = "".join(word[:level])
                print(prefix+res)
            else:
                print("".join(word[:level]))

        for i in range(26):
            if curr_node.children[i] is not None:
                word.insert(level, chr(i + ord('a')))
                self.display_util(curr_node.children[i], word, level+1, prefix)


    def display(self):
        word = []
        level = 0

        return(self.display_util(self.root, word, level))

    def prefix_matched_words_trie(self, prefix):
        result = []
        curr_node = self.root

        for i in range(len(prefix)):
            if prefix[i].isalpha():
                index = self._char_to_index(prefix[i])
                if curr_node.children[index]:
                    curr_node = curr_node.children[index]
                else:
                    print("Intended prefix is not found in Trie")
                    return result
        # Now the curr_node is at the end of the prefix word.
        # We need to print all the words from end of prefix

        self.display_util(curr_node, result, 0, prefix="pizza")



def main():
    strlist = ['Pizza Hut', 'Pieology', 'OPA', 'Pizza my heart', 'PastaPlace', 'pizzaria']
    prefix = "Pizza"

    print(prefix_matched_words_pythonic(strlist, prefix))

    t = Trie()

    for word in strlist:
        t.add_word(word.lower())

    print("**** Printing Trie *****")
    t.display()

    print("**** Printing Prefixed Matched words *****")
    t.prefix_matched_words_trie("pizza")

if __name__ == '__main__':
    main()


