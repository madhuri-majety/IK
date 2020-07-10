#! /usr/bin/python3

"""
Insertion Sort:
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands

Crux:
pick element a[i] and insert it into sorted sequence arr[0..i-1]

Slightly better algorithm than selection and bubble sort - Because, the number of comparisons and shifts made in
insertion sort are way less than selection and bubble sort

Time Complexity: O(n*n)

Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes
minimum time (Order of n) when elements are already sorted.

Algorithmic Paradigm: Incremental Approach

Sorting In Place: Yes

Stable: Yes

Online: Yes

Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted,
 only few elements are misplaced in complete big array.
"""

def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]

        hole = i
        while (hole>0 and a[hole-1] > value):
            a[hole] = a[hole-1]
            hole = hole-1
        a[hole] = value

def insertion_sort_rec(a, n):
    if n <= 1:
        return

    insertion_sort_rec(a, n-1)

    last = a[n-1]
    hole = n-2

    while (hole >=0 and a[hole] > last):
        a[hole+1] = a[hole]
        hole = hole - 1
    a[hole+1] = last



list = [9,7,6,15,16,5,10,11]
print("Before Sorting iteratively", list)
insertion_sort(list)
print("After sorting iteratively", list)
list1 = [9,7,6,15,16,5,10,11]
print("Before Sorting recursively", list1)
insertion_sort_rec(list1, len(list1))
print("After sorting recursively", list1)
