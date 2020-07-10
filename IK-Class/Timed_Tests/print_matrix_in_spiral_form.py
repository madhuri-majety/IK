"""

Print a given matrix in spiral form

Given a 2D array, print it in spiral form. See the following examples.

Examples:

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

https://www.youtube.com/watch?v=siKFOI8PNKM

"""
from __future__ import print_function

def print_matrix_spiral(A, rows, cols):
    """
    We will use four loops which prints all the elements. Every loop defines a single direction.
    First loop: left to right, enumarate it as dir = 0
    Second loop : top to bottom, enumarate it as dir = 1
    Third loop: right to left, enumerate it as dir = 2
    Fourth loop: bottom to top, enumerate it as dir = 3

    Will maintian four variables to mark the boundaries of untraversed matrix. (top, bottom, left, right)
    :param A:
    :param rows:
    :param cols:
    :return:
    """
    # Variables to mark the boundaries of untraversed matrix
    top = 0         # First row
    bottom = rows-1 # Last row
    left = 0        # First column
    right = cols-1  # Last column
    dir = 0         # Starting direction would be from left to right

    while (top <= bottom and left <= right):
        # Direction 0: traverse from left to right and then discard the top row
        if dir == 0:
            for i in range(left, right+1):
                print(A[top][i], end=" ")
            top += 1
            #dir = 1
        elif dir == 1:
            for j in range(top, bottom+1):
                print(A[j][right], end=" ")
            right -= 1
            #dir = 2
        elif dir == 2:
            #print("Left is :{}".format(left))
            for k in range(right, left-1, -1):
                print(A[bottom][k], end=" ")
            bottom -= 1
            #dir = 3
        elif dir == 3:
            for l in range(bottom, top-1, -1):
                print(A[l][left], end=" ")
            left += 1
            #dir = 0
        dir = (dir+1)%4

def print_sprial_matrix_recurive(A, top, left, bottom, right):
    # Base case: If top or left lies outside the matrix
    if top >= bottom and left >= right:
        return

    # Print first row
    for i in range(left, right+1):
        print(A[top][i], end=" ")

    # Print Last column
    for j in range(top+1, bottom+1):
        print(A[j][right], end=" ")

    # Print Last Row, if last and first row are not same
    if top != bottom:
        for k in range(right-1, left-1, -1):
            print(A[bottom][k], end=" ")

    # Print fist column, if first column is not equal to last column
    if left != right:
        for l in range(bottom-1, top, -1):
            print(A[l][left], end=" ")

    print_sprial_matrix_recurive(A, top+1, left+1, bottom-1, right-1)


def main():
    a =  [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

    a1 = [ [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]

    print_matrix_spiral(a, len(a), len(a[0]))
    print("\n\n")
    print_matrix_spiral(a1, len(a1), len(a1[0]))

    print("\n\n\n\n")
    print("Printing recursively")
    print_sprial_matrix_recurive(a, 0, 0, len(a)-1, len(a[0])-1)
    print("\n")
    print_sprial_matrix_recurive(a1, 0, 0, len(a1)-1, len(a1[0])-1)


if __name__ == '__main__':
    main()
