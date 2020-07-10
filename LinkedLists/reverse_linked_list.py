"""
Reverse a linked list

Iterative Method:
- Initialize three pointers prev as NULL, next as NULL and curr to head
- Iterate through the linked list. In loop do the following:
     - Move the next node pointer to the next of current node
     - Move current's next pointer to prev node (This is where actual reversing is happening)
     - Move prev node pointer to current node
     - Move current node to next node.

Recursive Method:
- Divide the list into two parts - first node and rest of the linked list
- Call reverse for rest of the linked list
- Link rest to first
- Fix head pointer
"""

from singly_linked_list import LinkedList, Node

def reverse(llist):
    head = llist.get_head()
    prev = None
    curr = llist.get_head()

    while curr is not None:
        next = curr.get_next()
        curr.set_next(prev)
        prev = curr
        curr = next

    llist.set_head(prev)

def reverse_rec_util(llist, curr, prev):
    if curr.get_next() is None:
        llist.set_head(curr)
        curr.set_next(prev)
        return

    next = curr.get_next()
    curr.set_next(prev)

    reverse_rec_util(llist, next, curr)

def reverse_rec(llist):
    if llist.get_head() is None:
        return

    reverse_rec_util(llist, llist.get_head(), None)

def main():
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)
    llist.append(10)
    llist.insert(llist.get_head().get_next(), 5)

    llist.print_list()
    print("Reversing a list")
    reverse(llist)
    llist.print_list()

    print("Reversing a list again using recursion")
    reverse_rec(llist)
    llist.print_list()

if __name__ == '__main__':
    main()
