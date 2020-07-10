"""
Sample script to illustrate race conditions with threads

Critical Section: Refers to the part of the program where the shared resource is accessed
Race Condition: A race condition occurs when two or more threads try to access the shared resource and
they try to change it at the same time. As a result, the values of variables may be unpredictable
and vary depending on the timing of the context switches of the processes
"""

import threading
import os

# Global Variable (Shared resource)
x = 0

def increment():
    """
    Increament the value of global variable x
    :return:
    """
    global x
    x += 1

def thread_task():
    """
    Call increment function 100000 times
    :return:
    """
    for _ in range(100000):
        increment()

def main_task():
    #print("PID of the process that invoked this task: {}".format(os.getpid()))

    global x
    # Setting it to 0
    x = 0

    # Creating threads
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))


