#! /usr/bin/python3
import sys

def sum_rec(num):
    if num == 0:
        return 0
    else:
        return (num + sum_rec(num-1))

def main():
    if len(sys.argv) <= 1:
        print("No Command line arguments. Please enter the number")
        exit()
    else:
        print("Name of the script is {}".format(sys.argv[0]))
        print("Finding the sum for number {}".format(int(sys.argv[1])))
        print("Sum is {}".format(sum_rec(int(sys.argv[1]))))

if __name__ == '__main__':
    main()
