#! /usr/bin/python3

"""
Recursively find the subsets of a string
- Enumerate all subsets of input

Solving recursively:
- Seperate one element from input
- Can include in current subset or not
- Recursively form subsets including it
- recursively form subsets not including it
- Base case when input string is empty
"""

def subset(sofar, rest):
    if len(rest) == 0:
        print(sofar)
    else:
        subset(sofar+rest[0], rest[1:])
        subset(sofar, rest[1:])


str1 = str(input("Input the string: "))
print("Inputted string is ", str1)
print("Printing subsets")
subset(" ",str1)
