"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionIterative(object):
    def add_two_numbers_iterative(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        result = curr = ListNode(-1)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry//10

        return result.next

    def print_ll(self, root):
        curr = root
        result = []
        while curr is not None:
            result.append(curr.val)
            curr = curr.next

        print(result)


class SolutionRecursive(object):
    def add_two_numbers_recursively(self, l1, l2, c = 0):
        val = l1.val + l2.val + c
        res = ListNode(val % 10)
        c = val //10

        if l1.next or l2.next or c:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            res.next = self.add_two_numbers_recursively(l1.next, l2.next, c)

        return res

    def print_ll(self, root):
        curr = root
        result = []
        while curr is not None:
            result.append(curr.val)
            curr = curr.next

        print(result)



def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(5)

    itersol = SolutionIterative()
    sum = itersol.add_two_numbers_iterative(l1, l2)
    itersol.print_ll(sum)

    recursol = SolutionRecursive()
    sum = recursol.add_two_numbers_recursively(l1, l2)
    recursol.print_ll(sum)


if __name__ == '__main__':
    main()
