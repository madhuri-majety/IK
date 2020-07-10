"""
Given two Binary Trees, write a function that returns true if two trees are mirror of each other, else false.
For example, the function should return true for following input trees.

https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/

Algorithm:
For two trees a and b to be mirror the following 3 conditions has to be met
- Root of both a and b should be same
- Left subtree of a and right subtree of b should be mirror
- Right subtree of b and left subtree of a should be mirror
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_mirror(a, b):
    # Base case 1: If both a and b are None then they are same
    if a is None and b is None:
        return True

    # Base Case 2: If one of them is None then there is a mismatch
    if a is None or b is None:
        return False

    return a.data == b.data and are_mirror(a.left, b.right) and are_mirror(a.right, b.left)

if __name__ == '__main__':
    root1 = Node(1)
    root2 = Node(1)

    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)

    if are_mirror(root1, root2):
        print ("Yes")
    else:
        print ("No")



