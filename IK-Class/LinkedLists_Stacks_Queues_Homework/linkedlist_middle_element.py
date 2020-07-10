"""
Find the middle element in a singly linked list
"""

from IK.LinkedLists.singly_linked_list import LinkedList, Node

def find_middle(llist):
    slow_ptr = llist.get_head()
    fast_ptr = llist.get_head()
    head = llist.get_head()
    if head is None:
        return

    while fast_ptr is not None and fast_ptr.get_next() is not None:
        slow_ptr = slow_ptr.get_next()
        fast_ptr = fast_ptr.get_next().get_next()

    return slow_ptr.get_data()

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

    print(find_middle(llist))

    llist.delete_node(2)
    llist.print_list()

    print(find_middle(llist))


if __name__ == '__main__':
    main()