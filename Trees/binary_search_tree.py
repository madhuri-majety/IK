""""
BST: A binary tree in which for each node, value of all the nodes in left
subtree is less than or equal to root and right subtree is greater than root

Pseudo Code:


"""
from collections import deque

import sys

class BstNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def getMin(root):
    current = root

    if root is None:
        print("Tree is empty")
        return -1

    while(current.left is not None):
        current = current.left

    return current.data

def getMax(root):
    current = root

    if root is None:
        print("Tree is emppty")
        return -1

    while (current.right is not None):
        current = current.right

    return current.data

def getMinRecursive(root):
    if root is None:
        print("Error: Tree is empty")
        return -1
    elif root.left is None:
        return root.data
    else:
        return getMinRecursive(root.left)

def getMaxRecursive(root):
    if root is None:
        print("Error: Tree is empty")
        return -1
    elif root.right is None:
        return root.data
    else:
        return getMaxRecursive(root.right)

def search(root, data):
    if root is None:
        return False
    elif root.data == data:
        return True
    elif data <= root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)

def findHeight(root):
    if root is None:
        return 0
    else:
        leftheight = findHeight(root.left)
        rightheight = findHeight(root.right)
        return max(leftheight, rightheight) + 1

def bfs_traversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        curr_node = q.popleft()
        print(curr_node.data)
        if curr_node.left:
            q.append(curr_node.left)
        if curr_node.right:
            q.append(curr_node.right)

def inorder_iterative(root):
    """
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then
        a) Pop the top item from stack.
        b) Print the popped item, set current = popped_item->right
        c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.
    :param root:
    :return:
    """
    current = root
    stack = []

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break

def isBSTUtil(root, min_value, max_value):
    if root is None:
        return True
    if (root.data >= min_value and root.data < max_value and
        isBSTUtil(root.left, min_value, root.data) and
        isBSTUtil(root.right, root.data, max_value)):
        return True
    else:
        return False

def isBinarySearchTree(root):
    INT_MIN = -sys.maxsize
    INT_MAX = sys.maxsize
    return isBSTUtil(root, INT_MIN, INT_MAX)

def delete_node(root, data):
    if root is None:
        return
    elif (data < root.data):
        root.left = delete_node(root.left, data)
    elif (data > data.root):
        root.right = delete_node(root.right, data)
    else:
        # This is the root to be deleted so follow all 3 cases
        # Case 1: No Child
        if root.left is None and root.right is None:
            root = None
            return root
        # Case 2: 1 Child
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp


        # Case 3: Having two children
        else:
            # Get the inorder successor(min in right subtree)
            temp = getMinRecursive(root.right)
            # Copy the inorder successor's node content to this node
            root.data = temp.data
            # Delete the inorder successor
            root.right = delete_node(root.right, temp.data)
    return root






if __name__ == "__main__":
    r = BstNode(50)
    insert(r, BstNode(30))
    insert(r, BstNode(20))
    insert(r, BstNode(40))
    insert(r, BstNode(70))
    insert(r, BstNode(60))
    insert(r, BstNode(80))
    insert(r, BstNode(90))

    print("Printing if the tree is BST or not: ")
    print(isBinarySearchTree(r))

    inorder(r)

    print(search(r, 20))
    print(search(r, 100))

    preorder(r)
    print("\n\n")
    postorder(r)

    print("\n\n")
    print("Height of Tree is ", findHeight(r))

    print("\n\nPrinting BFS/Level Order traversal ")
    bfs_traversal(r)

    print("\n\nInorder Iterative traversal")
    inorder_iterative(r)

    print("\nInorder recursive")
    inorder(r)

    print("\nPreorder Traversal")
    preorder(r)

    print("\nPostorder Traversal")
    postorder(r)

