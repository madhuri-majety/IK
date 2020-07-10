"""
Wirte a script to return the most frequent words in a flle
"""

import heapq
from collections import Counter
import re

class FileProcessing(object):
    def most_frequent_words_hash(self, filename):

        h = self.get_word_map_from_file(filename)
        print h

        print("************")
        print("With heapq module: ", heapq.nlargest(2, h, key=lambda h : h[1]))  # *****************

        print("\n\n%%%%%%%%%%%%%%")
        print("With build-in heapify: ", self.get_nlargest(h, 2))

    def get_word_map_from_file(self, file):
        with open(file, 'r') as fh:
            data = fh.read()

        # ***** To remove non-alphabets and non-digits use regular expression split than string split *******
        words = re.split('\W+', data.lower())
        count_map = {}
        for item in words:
            if item:
                count_map[item] = count_map.get(item, 0) + 1    # *******************************

        return count_map.items()


    def get_nlargest(self, iter, n):
        heap = []

        # Initialize heap with n elements from iter
        for i in range(n):
           heap.append(iter[i])
        #print("Heap with N elements: {}".format(heap))

        # Min heapify the list so the smallest value floats up to the root
        for i in range(len(heap)//2-1, -1, -1):
            self.min_heapify(heap, len(heap), i)
        #print("Heap after heapifying: {}".format(heap))

        # Now compare rest of the elements and if elements are greater than
        # root then replace root and min_heapify
        for i in range(n, len(iter)):
            if iter[i][1] > heap[0][1]:  # ***************************** #
                heap[0] = iter[i]
                self.min_heapify(heap, len(heap), 0)

        return heap

    def min_heapify(self, iter, size, index):
        smallest = index
        left = (2*index) + 1
        right = (2*index) + 2

        if left < size and iter[left][1] < iter[smallest][1]:
            smallest = left

        if right < size and iter[right][1] < iter[smallest][1]:
            smallest = right

        if smallest != index:
            iter[smallest], iter[index] = iter[index], iter[smallest]
            self.min_heapify(iter, size, smallest)


    def pythonic_way_most_common(self, file):
        """
        Use Counter module from collections which will take iterable as a input argument.
        most_frequent(n) api can report the n frequently used elements in iterable.
        :param file:
        :return:
        """
        #h = self.get_word_map_from_file(file)
        with open(file, 'r') as fh:
            data = fh.read()

        # ***** To remove non ascii characters use regular expression split than string split *******
        words = re.split('\W+', data.lower())

        counter = Counter(words)

        print counter.most_common(2)

def main():
    file = "input.txt"
    fp = FileProcessing()
    fp.most_frequent_words_hash(file)

    print(" \n*** Using Python Counter Module ***")
    fp.pythonic_way_most_common(file)

if __name__ == '__main__':
    main()

