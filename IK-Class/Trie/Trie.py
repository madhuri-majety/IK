"""
Implement Trie to insert, search and delete
https://www.geeksforgeeks.org/trie-insert-and-search/

Using Search Trie complexity is O(M), However the penalty is on storage requirements

"""
ALPHABET_SIZE = 26

class TrieNode(object):
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE
        self.is_end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        node = TrieNode()
        return node

    def _char_to_index(self,ch):
        # This funcation will return the relative order of characters
        # with starting index as 0 and that char at index 0 is 'a'
        return (ord(ch) - ord('a'))

    def insert(self, key):
        crawl = self.root
        length = len(key)

        for char in range(length):
            index = self._char_to_index(key[char])

            # If current character is not present
            if not crawl.children[index]:
                crawl.children[index] = self.get_node()
            crawl = crawl.children[index]

        # Mark last char as leaf node
        crawl.is_end_of_word = True

    def search(self, key):
        crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]

        if crawl != None and crawl.is_end_of_word:
            return True

    def has_no_children(self, node):
        for i in range(ALPHABET_SIZE):
            if node.children[i] is not None:
                return False
        return True

    def remove_util(self, key, curr_node, length, level):
        deleted_self = False

        if curr_node is None:
            print("Key does not exist")
            return deleted_self

        # Base case: If we have reached at the node which points to the
        # alphabet at the end of the key
        if level == length:
            # If there are no nodes ahead of this node
            # in this path then we can delete this node
            if self.has_no_children(curr_node):
                curr_node = None
                deleted_self = True

            else:
                curr_node.is_end_of_word = False
                deleted_self = False
        else:
            index = self._char_to_index(key[level])
            child_node = curr_node.children[index]
            child_deleted = self.remove_util(key, child_node, length, level + 1)

            if child_deleted:
                # Making children pointer to None as child is deleted.
                curr_node.children[index] = None

                # If this is end of word that means this is part of another key
                # and hence we cannot delete this node and its parent path nodes
                if curr_node.is_end_of_word:
                    deleted_self = False

                # If child node is deleted but if this node has more children then this
                # node must be part of another key. We cannot delete this node
                elif not self.has_no_children(curr_node):
                    deleted_self = False
                # Safely delete this node
                else:
                    curr_node = None
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    def remove(self, key):
        """
         ******* FIX IT ********
         Delete a key in Trie: During the delete operation we delete the key from bottom up approach using recursion.
         The following are possible conditions when deleting a trie
         Key doesnt exist in the trie DS. Delete operation should not modify trie.
         Key present as unique key (no part of key contains another key(prefix) nor the key itself in not the prefix
         of another key). In this case remove all nodes of that key
         Key is subset of longer keys in trie, then unmark the end of word flag to remove the reference of the key
         Key is superset of prefix keys or longest prefix key which  means having other keys inside the key we are
         looking for. In this case delete nodes from end of key until first leaf node of longest prefix key
         ********** https://www.ideserve.co.in/learn/trie-delete ***********
        :param key:
        :param depth:
        :return:
        """
        curr_node = self.root
        depth = 0

        if not curr_node or not key:
            print("Null Key or Trie is empty")
            return

        self.remove_util(key, curr_node, len(key), depth)
        return

    def display_util(self, curr_node, word, level):
        # Base case: If the curr node is end of word then print the word
        if curr_node.is_end_of_word:
            print("".join(word[:level]))

        for i in range(ALPHABET_SIZE):
            if curr_node.children[i]:
                word.insert(level, (chr(i + ord('a'))))
                self.display_util(curr_node.children[i], word, level + 1)


    def display(self):
        word = []
        print("*** Display():  {}".format(word))
        level = 0
        self.display_util(self.root, word, level)


def main():
    keys = ["the", "a", "there", "answer", "any", "by", "their"]
    output = ["Not present in trie", "Present in Trie"]

    # Trie Object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ------- {}".format("the", output[t.search("the")]))
    print("{} ------- {}".format("these", output[t.search("these")]))
    print("{} ------- {}".format("there", output[t.search("there")]))
    print("{} ------- {}".format("their", output[t.search("their")]))
    print("{} ------- {}".format("thaw", output[t.search("thaw")]))

    # Delete few keys
    t.remove("there")

    # Search for deleted key
    print("After deleting the key")
    print("{} ------- {}".format("there", output[t.search("there")]))
    print("{} ------- {}".format("their", output[t.search("their")]))
    print("{} ------- {}".format("the", output[t.search("the")]))

    # Display words in Trie
    print("**** Printing Contents in Trie **** ")
    t.display()


if __name__ == '__main__':
    main()



