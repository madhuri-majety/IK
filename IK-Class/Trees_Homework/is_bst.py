"""
Given a binary tree check if it is a BST or not
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(curr, l= None, r= None):
    if curr is None:
        return True

    if l is not None and curr.data <= l.data:
        return False

    if r is not None and curr.data >= r.data:
        return False

    return is_bst(curr.left, l, root) and is_bst(curr.right, root, r)

# Driver Code
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    #root.right.left = Node(1)
    root.right.right = Node(4)
    root.right.left = Node(40)
    if (is_bst(root,None,None)):
        print("Is BST")
    else:
        print("Not a BST")

