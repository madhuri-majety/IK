"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.



Note:

    You must return the copy of the given head as a reference to the cloned list.

https://leetcode.com/problems/copy-list-with-random-pointer/solution/

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class RandomPointerList(object):
    def __init__(self):
        # Visited dictionary to store the old nodes of a cloned list
        self.visited = {}

    def copy_list_with_random_pointer(self, head):
        """

        :param head:
        :return:
        """
        if head == None:
            return None

        # If we have already processed the current node, then we simply
        # return the node from the cloned version of it
        if head in self.visited:
            return self.visited[head]

        # If not create the new cloned node and add it to the visited dictionary
        # This is needed since there might be loops during traversal due to randomness
        # of random pointers and this would help us avoid them.
        else:
            node = ListNode(head.val)

        self.visited[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer
        # and then from the random pointer
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created
        node.next = self.copy_list_with_random_pointer(head.next)
        node.random = self.copy_list_with_random_pointer(head.random)

        return node

def main():
