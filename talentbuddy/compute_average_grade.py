from __future__ import division
import math

"""
Average grade

Given an array with all final grades for a course

Your task is to

    write a function that computes the average of all the grades in the array and prints this number to standard output (stdout)
    the result must be rounded downwards to the nearest integer (e.g. both 7.1 and 7.9 are rounded to 7)

Note that your function will receive the following arguments:

    grades
        which is the list of grades, represented as integer numbers

Data constraints

    the length of the array given as input will not exceed 1000 elements

Example
Input 	                                    Output

grades: 1, 2, 8, 4, 5, 8, 3                 4
"""

def compute_average_grade(grades):
    total = sum(grades)
    average = int(math.floor(total/len(grades)))
    print average
    
list = [1, 2, 8, 4, 5, 8, 3]
compute_average_grade(list)