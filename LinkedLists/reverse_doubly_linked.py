"""
Reverse a doubly linked list

Approach:
Just swap prev and next pointers of all nodes, change prev of the head and
change the head pointer in the end
"""

from doubly_linked_list import DLinkedList

def reverse_dll(dllist):
    temp = None
    curr = dllist.get_head()

    while curr is not None:
        temp = curr.get_prev()
        curr.set_prev(curr.get_next())
        curr.set_next(temp)
        curr = curr.get_prev()

    if temp is not None:
        dllist.set_head(temp.get_prev())


def main():
    mylist = DLinkedList()
    mylist.append(7)
    mylist.push(6)
    mylist.push(1)
    mylist.append(4)
    mylist.insert_after(mylist.get_head().get_next(), 8)
    print("Created DLL is:")
    mylist.print_list()

    print("After the deleting the node")
    mylist.delete_node(mylist.get_head().get_next())
    mylist.print_list()

    print("Reversing a doubly linked list")
    reverse_dll(mylist)
    mylist.print_list()

if __name__ == '__main__':
    main()