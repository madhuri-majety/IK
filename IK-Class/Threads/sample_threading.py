"""
https://www.geeksforgeeks.org/multithreading-python-set-1/

Pytjon program to illustrate the concept of threading
"""

import threading


def cube(num):
    """
    Function to print cube of a number
    :param num:
    :return:
    """
    print("Cube: {}".format(num*num*num))

def square(num):
    """
    Function to print the square of a number
    :param num:
    :return:
    """
    print("Square: {}".format(num*num))

def main():
    # Creating two threads
    t1 = threading.Thread(target=cube, args=(10,))
    t2 = threading.Thread(target=square, args=(10,))

    # Starting Thread1
    t1.start()

    # Starting Thread2
    t2.start()

    # Wait until Thread1 is completely executed
    t1.join()

    # Wait until Thread2 is completely executed
    t2. join()

    # both threads are completely executed
    print("Done!")

if __name__ == "__main__":
    main()

