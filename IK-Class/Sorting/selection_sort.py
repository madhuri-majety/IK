#! /usr/bin/python3

"""
Selection Sort:
Selection sort sorts an array by repeatedly finding the min elelment from unsorted part and putting
at the beginning. The algorithm maintains two subarrays on a given array
1. The sorted array in the beginning
2. The unsorted array following the sorted array

Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)

Stable : No

Selection sort makes O(n) swaps which is minimum among all sorting algorithms mentioned above.

"""

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def selection_sort(list):
    num_elems = len(list)
    for i in range(num_elems-1):
        imin = i
        for j in range(i+1, num_elems):
            if list[j] <= list[imin]:
                imin = j
        #swap(list, i, imin)
        list[i], list[imin] = list[imin], list[i]


list = [2,7,1,4,-9,3,10]
char_list = ["Madhu", "Ritu", "Rithika", "Sumanth", "Jaya"]
print("List before sorting: ", char_list)
selection_sort(char_list)
print("After sorting the list: ", char_list)
