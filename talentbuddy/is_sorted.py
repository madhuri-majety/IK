"""
Your task is to

    write a function that checks whether the grades received by each student are in ascending order
    your function must print to standard output (stdout):
        1 if the grades are in ascending order (e.g. 1, 3, 3, 7)
        0 if the grades are not in ascending order (e.g. 1, 3, 7, 3)

Note that your function will receive the following arguments:

    grades
        which is an array containing the grades of the student

Data constraints

    the length of the array given as input will not exceed 1000 elements

Example
Input 	                       Output

grades: 1, 3, 3, 7              1
"""

def is_sorted(grades):
    print 1 if grades == sorted(grades) else 0
    
list=[1,3,3,7]
is_sorted(list)
is_sorted([1,7,3,2])
        