"""
https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
http://www.cs.usfca.edu/~brooks/S04classes/cs245/lectures/lecture11.pdf

Serialization is to store tree in a file so that it can be later restored.
The structure of tree must be maintained.
Deserialization is reading tree back from file.

******* https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/

The serialization of a Binary Search Tree is essentially to encode its values and more importantly its structure.
One can traverse the tree to accomplish the above task. And it is well know that we have two general
strategies to do so:

Breadth First Search (BFS)

    We scan through the tree level by level, following the order of height, from top to bottom.
    The nodes on higher level would be visited before the ones with lower levels.

Depth First Search (DFS)

    In this strategy, we adopt the depth as the priority, so that one would start from a root
    and reach all the way down to certain leaf, and then back to root to reach another branch.

    The DFS strategy can further be distinguished as preorder, inorder, and postorder depending on the
    relative order among the root node, left node and right node.

A delimiter(like None) needs to added to to indicate that the node is a leaf node

We start from the root, node 1, the serialization string is 1,.
Then we jump to its left subtree with the root node 2, and the serialization string becomes 1,2,.
Now starting from node 2, we visit its left node 3 (1,2,3,None,None,)
and right node 4 (1,2,3,None,None,4,None,None) sequentially.
Note that None,None, appears for each leaf to mark the absence of left and right child node,
this is how we save the tree structure during the serialization.
And finally, we get back to the root node 1 and visit its right subtree which happens to be a leaf node
5. Finally, the serialization string is done as 1,2,3,None,None,4,None,None,5,None,None,.


Time complexity : in both serialization and deserialization functions,
we visit each node exactly once, thus the time complexity is O(N),
where N is the number of nodes, i.e. the size of tree.

Space complexity : in both serialization and deserialization functions,
we keep the entire tree, either at the beginning or at the end, therefore,
the space complexity is O(N).

"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def serialize_util(root, string):
    """
    Do the pre order traversal and store it to the string
    :param root:
    :param string:
    :return:
    """
    # Base case if a leaf node is reached then mark its left and right child as None
    if root is None:
        string += "None,"

    else:
        string += str(root.data) + ','
        string = serialize_util(root.left, string)
        string = serialize_util(root.right, string)

    return string

def serialize(root):
    string = ""
    return serialize_util(root, string)

def deserialize_util(dl):
    # Base case: if list element is None that means that is a leaf node and return None
    if dl[0] == 'None':
        dl.pop(0)
        return None


    root = Node(dl[0])
    dl.pop(0)
    root.left = deserialize_util(dl)
    root.right = deserialize_util(dl)

    return root

def print_pre_order(root):
    if root is not None:
        print(root.data)
        print_pre_order(root.left)
        print_pre_order(root.right)


def deserialize(data):
    data_list = data.split(",")
    root = deserialize_util(data_list)
    return root

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    print(serialize(root))
    new_root = deserialize(serialize(root))
    print_pre_order(new_root)
