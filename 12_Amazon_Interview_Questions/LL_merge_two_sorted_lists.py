"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionIterative(object):
    def merge_two_sorted_list_iter(self, l1, l2):
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        result = ListNode(-1)
        prev = result


        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return result.next

    def print_ll(self, root):
        curr = root

        while curr:
            print(curr.val, end="->")
            curr = curr.next

        print("None")

class SolutionRecursive(object):
    def merge_two_lists_recur(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            res = l1
            res.next = self.merge_two_lists_recur(l1.next, l2)
        else:
            res = l2
            res.next = self.merge_two_lists_recur(l1, l2.next)

        return res

    def print_ll(self, root):
        curr = root

        while curr:
            print(curr.val, end="->")
            curr = curr.next

        print("None")

def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    itersol = SolutionIterative()
    itersol.print_ll(itersol.merge_two_sorted_list_iter(l1, l2))

    l3 = ListNode(1)
    l3.next = ListNode(2)
    l3.next.next = ListNode(4)
    l3.next.next.next = ListNode(5)

    l4 = ListNode(1)
    l4.next = ListNode(3)
    l4.next.next = ListNode(4)

    recursol = SolutionRecursive()
    merge = recursol.merge_two_lists_recur(l3, l4)
    recursol.print_ll(merge)

if __name__ == '__main__':
    main()




