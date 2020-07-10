"""
Given a binary tree find the deepest node in it.
Input : Root of below tree
            1
          /   \
         2      3
        / \    / \
       4   5  6   7
                   \
                    8
Output : 8

Input : Root of below tree
            1
          /   \
         2      3
               /
              6
Output : 6

The idea is to do Inorder traversal of given binary tree.
While doing Inorder traversal, we pass level of current node also.
We keep track of maximum level seen so far and value of deepest node seen so far.

"""

class newNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def find(root, level, max_level, res):
    if root is not None:
        level += 1
        # Inorder traversal and update max level
        find(root.left, level, max_level, res)

        if level > max_level[0]:
            max_level[0] = level
            res[0] = root.data

        find(root.right, level, max_level, res)


def deepest_node(root):
    res = [-1]
    max_level = [-1]
    level = 0

    find(root, level, max_level, res)

    return (max_level[0], res[0])

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(6)
    root.right.left.right = newNode(7)
    root.right.right.right = newNode(8)
    root.right.left.right.left = newNode(9)
    print(deepest_node(root))
