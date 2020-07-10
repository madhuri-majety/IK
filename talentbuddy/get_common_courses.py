"""
 A teacher wants to compare the performance of two students. To understand them better, hes looking at all the other courses they took, but its hard to spot the common courses just from a glance.

Given two arrays that contain the course IDs of two different students

Your task is to

    write a function that prints to standard output (stdout) all the course IDs that are contained in both arrays, sorted in ascending order, one per line

Note that your function will receive the following arguments:

    courses1
        which is the list of course IDs for the first student
    courses2
        which is the list of course ids for the second student

Data constraints

    the length of the array given as input will not exceed 1000 elements

Example
Input 	Output

courses1: 1, 2, 8, 4, 5, 8, 3
courses2: 8, 2, 2, 7, 10
	

2
8
"""

def get_common_courses(courses1, courses2):
    common_list=[]
    for i in xrange(len(courses1)):
        for j i