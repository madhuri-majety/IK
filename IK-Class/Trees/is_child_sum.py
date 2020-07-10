"""

Check for Children Sum Property in a Binary Tree

Given a binary tree, write a function that returns true if the tree satisfies below property.

For every node, data value must be equal to sum of data values in left and right children.
Consider data value as 0 for NULL children. Below tree is an example

        10
       /  \
      8   2
    /  \  /
   3   5  2

https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_child_sum(node):
    if node is None or (node.left is None and node.right is None):
        return True

    left_child = 0
    right_child = 0

    if node.left is not None:
        left_child = node.left.data

    if node.right is not None:
        right_child = node.right.data

    return (node.data == left_child + right_child) and is_child_sum(node.left) and is_child_sum(node.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(2)

    if is_child_sum(root):
        print("The given tree satisfies the children sum property")
    else:
        print("The given tree does not satisfy the children sum property")

