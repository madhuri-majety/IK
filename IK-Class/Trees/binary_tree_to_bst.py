"""
Given a Binary Tree, convert it to a Binary Search Tree.
The conversion must be done in such a way that keeps the original structure of Binary Tree.

Solution:
Create temp array the stores inorder traversal of given binary tree. This step take O(n) time
Sort the array. Time complexity is O(logN) if most efficient sorting algorithm is picked.
Again do inorder traversal of tree and start coping array elements one by one. This step takes O(logN)
"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left =  None

def store_inorder(root, inorder):
    """
    Helper function to store inorder of a given binary tree
    :param root:
    :param inorder:
    :return:
    """
    # Base case
    if root is None:
        return

    store_inorder(root.left, inorder)
    inorder.append(root.data)
    store_inorder(root.right, inorder)


def count_nodes(root):
    if root is None:
        return 0

    return count_nodes(root.left) + count_nodes(root.right) + 1

def arr_to_bst(root, arr):
    # Base case
    if root is None:
        return
    #First update left subtree inorder
    arr_to_bst(root.left, arr)

    # Update binary trees data with new data from array
    root.data = arr[0]
    arr.pop(0)

    # Second update right subtree inorder
    arr_to_bst(root.right, arr)


def binary_tree_to_bst(root):
    # Base case:
    if root is None:
        return

    n = count_nodes(root)
    print("Number of nodes in given binary tree: {}".format(n))

    # First step store inorder traversal of binary tree
    arr = []
    store_inorder(root, arr)

    # Sort the array
    arr.sort()

    # Third step update the binary tree inorder with array elements
    arr_to_bst(root, arr)

def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)


def main():
    root = BSTNode(10)
    root.left = BSTNode(30)
    root.right = BSTNode(15)
    root.left.left = BSTNode(20)
    root.right.right = BSTNode(5)

    print("Priniting inoder of binary tree")
    print_inorder(root)

    # Convert the binary tree to BST inplace
    binary_tree_to_bst(root)

    print("Printing inorder of BST after conversion")
    print_inorder(root)

if __name__ == '__main__':
    main()
