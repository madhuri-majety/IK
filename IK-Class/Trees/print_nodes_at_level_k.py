"""
Print all nodes at level k
Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.

"""
from __future__ import print_function
from collections import deque

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_level_k_dfs(root, k):
    """
    Using DFS traversal, we can print the level k  values
    Time Complexity is O(N) as we are traversing back and forth to all node for finding level k
    :param root:
    :param k:
    :return:
    """
    if root is None:
        return
    if k == 0:
        print(root.data, end=" ")

    else:
        print_level_k_dfs(root.left, k-1)
        print_level_k_dfs(root.right, k-1)

def print_level_k_bfs(root, k):
    q = deque()
    q.append(root)
    q.append(-1)
    level = 0

    while q:
        cur_node = q.popleft()
        if cur_node == -1:
            q.append(-1)
            level += 1
        else:
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

        if level == k:
            break

    while q:
        cur = q.popleft()
        if cur != -1:
            print(cur.data, end=" ")
            

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    print("Priting level k items using DFS")
    print_level_k_dfs(root, 2)
    print("\n\nPriting level k items using BFS")
    print_level_k_bfs(root, 2)
