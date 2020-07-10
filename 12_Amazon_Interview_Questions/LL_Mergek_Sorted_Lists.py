"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


**** Below code works in the leetcode. Something wrong with the input here

"""

import heapq
from queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeKSortedMinHeap(object):
    def mergeKLists(self, lists):
        head = point = ListNode(-1)
        h = []
        for l in lists:
            if l:
                print(l.val)
                heapq.heappush(h, (l.val, l))
        while h:
            val, node = heapq.heappop(h)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(h, (node.val, node))

        print(self.print_dll(head.next))

    def merge_k_lists_pri_queue(self, lists):
        head = point = ListNode(-1)
        pq = PriorityQueue()

        for l in lists:
            if l:
                pq.put((int(l.val), l))
        while not pq.empty():
            val, node = pq.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                pq.put((int(node.val), node))

        print(self.print_dll(head.next))

    def print_dll(self, root):
        curr = root

        while curr:
            print(curr.val, end="->")
            curr = curr.next

        print("None")

def main():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    priqueue = MergeKSortedMinHeap()
    priqueue.merge_k_lists_pri_queue([l1, l2, l3])
    priqueue.mergeKLists([l1, l2, l3])

if __name__ == '__main__':
    main()



