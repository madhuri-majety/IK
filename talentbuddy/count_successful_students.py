"""
Successful students

Given an array with all final grades for a course and the minimum grade that a student needs to have in order to pass the course

Your task is to

    write a function that counts the number of students that passed and prints this number to standard output (stdout)

Note that your function will receive the following arguments:

    grades
        which is the list of grades, represented as integer numbers
    min_grade
        which is the minimum grade that a student can get, so that he passes the course

Data constraints

    the length of the array given as input will not exceed 1000 elements

Example
Input 	                                            Output

grades: 1, 2, 8, 4, 5, 8, 3
min_grade: 5                                        3
"""

def count_successful_students(grades, min_grade):
    count = sum([1 for x in grades if x>=min_grade])   
    print count
    
def count_successful_students_tb(grades, min_grade):
    print len([students for students in grades if students >= min_grade])
    
list = [1, 2, 8, 4, 5, 8, 3]
count_successful_students(list, 5)
count_successful_students_tb(list,5)