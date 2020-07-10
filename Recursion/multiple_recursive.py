#! /usr/bin/python3
import sys

def mutiple_of_three(num):
    if num == 1:
        return 3
    else:
        return mutiple_of_three(num-1) + 3

#number = input("Enter the number - ")
#print(mutiple_of_three(int(number)))

if len(sys.argv) <= 1:
    print("No command line arguments provided. Please input the number")
    exit()
else:
    print("Name of the script is {}".format(sys.argv[0]))
    print("Finding the multiple of 3 for number {}".format(sys.argv[1]))
    print("Value is {}".format(mutiple_of_three(int(sys.argv[1]))))
