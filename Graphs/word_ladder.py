"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

https://leetcode.com/problems/word-ladder/
https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/

***** Refer to Evernote for different approaches in detailed steps.

"""
from collections import defaultdict, deque
import time

class BFSPreProcessingList(object):
    def ladder_length(self, startw, endw, wordlist):
        if endw not in wordlist or not startw or not endw or not wordlist:
            return 0

        # Since all words are of same length
        wordlength = len(startw)

        # Preprocess the word list and store all the generic transformations
        # of a word in dictionary
        all_combo_dict = defaultdict(list)

        # Key is generic word
        # Value is a list of words which have the same intermediate generic word
        for word in wordlist:
            for l in range(wordlength):
                all_combo_dict[word[:l] + '*' + word[l+1:]].append(word)

        print(all_combo_dict)

        # BFS Search
        queue = deque()
        visited = {}

        # Make sure we dont form a cycle
        visited[startw] = True
        # Add the starting word and its level it started and if word is found this is the level returned
        queue.append((startw, 1))

        while queue:
            cur_word, cur_level = queue.popleft()

            for i in range(wordlength):
                # Form all the intermediate generic words for curr word
                intermediate_word = cur_word[:i] + '*' + cur_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    # If at any point we found our end word we can return with answer
                    if word == endw:
                        return cur_level + 1
                    else:
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, cur_level+1))

                # For space optimization,we can clear the intermediate word key from dictionary
                all_combo_dict[intermediate_word] = []

        return 0

class BFSOnDemand(object):
    def get_neighbors(self, curword, wordlist):
        result = []
        for word in wordlist:
            numdiff = 0
            for i in range(len(word)):
                if curword[i] != word[i]:
                    numdiff += 1

            if numdiff == 1:
                result.append(word)

        return result

    def ladder_length(self, startw, endw, wordlist):
        queue = deque()
        visited = {}

        # Append the current word to queue, update length and visited dictionary
        queue.append(startw)
        length = 0
        visited[startw] = True

        while queue:
            cur_word = queue.popleft()
            length += 1

            neighbors = self.get_neighbors(cur_word, wordlist)

            for neigh in neighbors:
                if neigh == endw:
                    return length
                else:
                    if neigh not in visited:
                        visited[neigh] = True
                        queue.append(neigh)

        return 0


def main():
    print("*** Printing using BFS Preprocessing ****")
    bfspreprocessing = BFSPreProcessingList()
    start_time = time.time()
    print(bfspreprocessing.ladder_length('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    end_time = time.time()
    print("Time elapsed for Preprocessing is : {}".format(end_time - start_time))
    print(bfspreprocessing.ladder_length('hit', 'cog', ["hot","dot","dog","lot","log"]))

    print("*** Printing using BFS On Demand Neighbors")
    bfsondemand = BFSOnDemand()
    start = time.time()
    print(bfsondemand.ladder_length('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    end = time.time()
    print("Time elapsed for on demand neighbors is : {}".format(end-start))
    print(bfsondemand.ladder_length('hit', 'cog', ["hot","dot","dog","lot","log"]))


if __name__ == '__main__':
    main()





