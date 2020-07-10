"""
Given a text file and a word, find the positions that the word occurs in the file.
 We will be asked to find the positions of many words in the same file, i.e. think precomputing with inverted index

The Inverted Index is the data structure used to support full text search over a set of documents.
It is constituted by a big table where there is one entry per word in all the documents processed,
along with a list of the key pairs: document id, frequency of the term in the document.

Implement using hash tables and also trie
"""
import re

class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False
        self.positions = []

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word, pos):
        crawl = self.root

        for char in word:
            index = self._char_to_index(char)
            if not crawl.children[index]:
                crawl.children[index] = TrieNode()
            crawl = crawl.children[index]

        crawl.end_of_word = True
        crawl.positions.append(pos)

    def get_positions(self, word):
        crawl = self.root

        for char in word:
            index = self._char_to_index(char)
            if not crawl.children[index]:
                return None
            crawl = crawl.children[index]

        return crawl.positions

    def search(self, word):
        crawl = self.root

        for char in word:
            index = self._char_to_index(char)
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]

        return crawl.end_of_word

    def display_trie(self):
        curr_node = self.root
        sofar = []
        level = 0

        self.display_trie_util(curr_node, sofar, level)

    def display_trie_util(self, curr_node, sofar, level):
        if curr_node.end_of_word:
            print("{} : {}".format("".join(sofar[:level]), curr_node.positions))


        for i in range(26):
            if curr_node.children[i]:
                sofar.insert(level, chr(i + ord('a')))
                self.display_trie_util(curr_node.children[i], sofar, level+1)


class InvertedIndex(object):
    def __init__(self, file):
        self.file = file
        self.hash_index = {}
        self.trie_index = Trie()

    def parse_file(self):
        with open(self.file, 'r') as fh:
            data = fh.read()

        words = re.split('\W+', data.lower())

        return words

    def create_index_in_hash(self):
        words = self.parse_file()

        for pos, word in enumerate(words):
            if word not in self.hash_index:
                self.hash_index[word] = [pos]
            else:
                self.hash_index[word].append(pos)

        print("Printing Inverted index stored in Hash : {}".format(self.hash_index))

    def query_index_in_hash(self, word):
        if word in self.hash_index:
            return self.hash_index[word]

        return None

    def create_index_in_Trie(self):
        words = self.parse_file()

        for pos, word in enumerate(words):
            self.trie_index.insert(word, pos)

        print("Printing Inverted Index stored in Trie:")
        self.trie_index.display_trie()

    def query_index_in_trie(self, word):
        return self.trie_index.get_positions(word)


def main():
    file = "/Users/sumanthkakaraparthi/Documents/MacPro-2019/Documents/scripts/Automation/inverted_index_file.txt"

    ii = InvertedIndex(file)

    ii.create_index_in_hash()
    ii.create_index_in_Trie()

    print("Getting index using Hash: {}".format(ii.query_index_in_hash("hashmap")))
    print("Getting index using Trie: {}".format(ii.query_index_in_trie("hashmap")))

if __name__ == '__main__':
    main()






