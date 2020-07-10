"""
Merge two sorted linked list

Recursive approach:
- Not to use in production code as it will use stack space which is proportional to the length of the lists
"""

from singly_linked_list import LinkedList, Node

def merge_ll(head1, head2):
    temp = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.get_data() <= head2.get_data():
        temp = head1
        temp.next = merge_ll(head1.get_next(), head2)
    else:
        temp = head2
        temp.next = merge_ll(head1, head2.get_next())

    return temp


def main():
    # Create linked list :
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)
    print("Printing List1:")
    list1.print_list()

    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = LinkedList()
    list2.append(5)
    list2.append(15)
    list2.append(18)
    list2.append(35)
    list2.append(60)
    print("Prining List2:")
    list2.print_list()

    # Create linked list 3
    list3 = LinkedList()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = merge_ll(list1.get_head(), list2.get_head())

    print(" Merged Linked List is : ", end="")
    list3.print_list()


if __name__ == '__main__':
    main()
