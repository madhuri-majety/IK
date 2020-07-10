"""
Given an n x n matrix and a number x, find position of x in the matrix if it is present in it.
 Else print not present. In the given matrix, every row and column is sorted in increasing order.
 The designed algorithm should have linear time complexity.

Table[i][j] <= Table[i][j + 1],
Table[i][j] <= Table[i + 1][j]

Example :

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output : present

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : not present

Brute force - search element by element. TC - O(n^2)
Optimal Solution: Traverse matrix diagnolly from top right corner. TC - O(n)
    - Start with top right element
    - Loop: compare this array element e with x
        - If x is greater than e, move down (increment row)
        - If x is less than e, move left (decrement column)
    - repeat above step until element e is found


"""

def two_dimensional_array_search(arr,x):
    r = 0
    c = len(arr[0])-1

    while(r < len(arr) and c >= 0):
        if arr[r][c] == x:
            return "present"
        if x > arr[r][c]:
            r += 1
        else:
            c -= 1

    return "not present"

def main():
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48]]

    q = [70, 50, 25, 37, 1]
    for i in q:
        print(two_dimensional_array_search(mat,i))

if __name__ == '__main__':
    main()
