"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.

Notes:
    This can be done recursively as the subset of linked list has to be reversed every time
"""
class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseNodesInKGroups(object):
    def reverse_nodes_in_k_groups(self, root, k):
        print("<<"+ str(root.val))
        curr = root
        next = None
        prev = None
        count = 0

        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            root.next = self.reverse_nodes_in_k_groups(next, k)

        return prev

    def print_ll(self, root):
        cur = root
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print('None')

class ReverseNodesInExactKGroups(object):
    """
    Imagine node reference is 100+number, numbers from 1 -> with k = 2
    reverse(101, 2)
    First Recursion:
            head = 101
            k = 2
            tail = 102
            post = reverse(103, 2) ==> Returns prev which is 104
            so head.next points to post which means 1 --> 4
    Second Recursion:
            head = 103
            k = 2
            tail = 104
            post = reverse(105, 2) ==> Returns prev which is 106
            so head.next points to post which means 3 --> 6
    Third Recursion:
            head = 105
            k = 2
            tail = 106
            post = reverse(107, 2) ==> Returns head(107) as the count of nodes is less than 2
            so 5 --> 7
    Fourth Recursion:
            head = 107
            k = 2
            tail = 107
            returns 107 (head)

    Put these calls in stack with stack variables and things will be easy to understand

    """
    def reverse_nodes_in_exact_k_groups(self, head, k):
        print("Head is {}".format(head.val))
        tail = head
        count = 0

        while tail:
            count += 1
            if count == k:
                break
            tail = tail.next
        if count < k:
            print("Count less than k. So returning {}".format(head.val))
            return head

        post = self.reverse_nodes_in_exact_k_groups(tail.next, k)

        prev = None
        curr = head
        count = 0
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        head.next = post

        print("Returning Prev value {}".format(prev.val))
        return prev

    def print_ll(self, root):
        cur = root
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print('None')




def main():
    l1 = LinkNode(1)
    l1.next = LinkNode(2)
    l1.next.next = LinkNode(3)
    l1.next.next.next = LinkNode(4)
    l1.next.next.next.next = LinkNode(5)
    #l1.next.next.next.next.next = LinkNode(6)
    #l1.next.next.next.next.next.next = LinkNode(7)

    reverse = ReverseNodesInKGroups()
    new = reverse.reverse_nodes_in_k_groups(l1, 3)
    reverse.print_ll(new)

    l2 = LinkNode(1)
    l2.next = LinkNode(2)
    l2.next.next = LinkNode(3)
    l2.next.next.next = LinkNode(4)
    l2.next.next.next.next = LinkNode(5)
    #l2.next.next.next.next.next = LinkNode(6)
    #l2.next.next.next.next.next.next = LinkNode(7)

    exact = ReverseNodesInExactKGroups()
    new_exact = exact.reverse_nodes_in_exact_k_groups(l2, 3)
    exact.print_ll(new_exact)



if __name__ == '__main__':
    main()

