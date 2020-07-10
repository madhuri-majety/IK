"""

Print path from root to a given node in a binary tree

Given a binary tree with distinct nodes(no two nodes have the same have data values).
The problem is to print the path from root to a given node x. If node x is not present then print "No Path".

Input :          1
               /   \
              2     3
             / \   /  \
            4   5  6   7

               x = 5

Output : 1->2->5

https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def has_path(root, x, arr):
    if root is None:
        return False

    arr.append(root.data)

    if root.data == x:
        return True

    if (has_path(root.left, x, arr) or has_path(root.right, x, arr)):
        return True

    # If we come here means, the element is not found in left or right subtree of a node
    arr.pop()

    return False


def print_path(root, x):
    arr = []

    if has_path(root, x, arr):
        print(arr)
    else:
        print("No path to {}".format(x))


if __name__ == '__main__':

    # binary tree formation
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 7
    print_path(root, x)
