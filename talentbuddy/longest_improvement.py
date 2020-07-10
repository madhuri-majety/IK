"""
Longest improvement

A student's performance in lab activities should always improve, but that is not always the case.

Since progress is one of the most important metrics for a student, lets write a program that computes the longest period of increasing performance for any given student.

For example, if his grades for all lab activities in a course are: 9, 7, 8, 2, 5, 5, 8, 7 then the longest period would be 4 consecutive labs (2, 5, 5, 8).

Given an array with the lab grades of a student

Your task is to

    write a function that computes and prints to standard output (stdout) the longest period of increasing performance for the student that has these grades

Note that your function will receive the following arguments:

    grades
        which is an array containing the grades of the student

Data constraints

    the length of the array given as input will not exceed 1000 elements

Example
Input 	                            Output

grades: 9, 7, 8, 2, 5, 5, 8, 7          4
"""

def longest_improvement(grades):
    prev_period = 0
    period = 0
    for i in xrange(len(grades)-1) :
        if grades[i+1] >= grades[i]:
            period = period+1
            continue
        else:
            if prev_period < period:
                prev_period = period
                period = 0
    print prev_period+1
    
longest_improvement([9, 7, 8, 2, 5, 5, 8, 7])
longest_improvement([1,2,3,4,5,6,7,8,9,1])