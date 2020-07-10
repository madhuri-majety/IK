"""
Sample program to illustrate the threading methods
"""

import threading
import os

def task1():
    print("Task1 is assigned to thread :{}".format(threading.current_thread().name))
    print("PID of process running task1: {}".format(os.getpid()))

def task2():
    print("Task2 is assigned to thread: {}".format(threading.current_thread().name))
    print("PID of process running task2: {}".format(os.getpid()))

def main():
    # Print PID of current process
    print("PID of process running main program: {}".format(os.getpid()))

    # Print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # Creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # Start threads
    t1.start()
    t2.start()

    # Wait for the threads to excute
    t1.join()
    t2.join()

    print("Done!")

if __name__ == "__main__":
    main()
