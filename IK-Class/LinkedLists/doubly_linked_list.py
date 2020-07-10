"""
A doubly linked list contains an extra pointer, typically called previous pointer, together
with next pointer and data which are there in singly linked list
"""
import gc

class Node(object):
    def __init__(self, d, n = None, p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, n):
        self.next_node = n

    def set_prev(self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class DLinkedList(object):
    def __init__(self, h = None):
        self.head = h
        self.size = 0

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def set_head(self, h):
        self.head = h

    def push(self, new_data):
        """
        Insert new node at the front of the list
        """
        new_node = Node(new_data)

        # Make next of new node as head and previous as None (already None)
        new_node.set_next(self.head)

        # Make prev of head to new node
        if self.head is not None:
            self.head.set_prev(new_node)

        # Move the head to point to the new node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """
        Given a node as prev_node, insert a new node after the given node
        """
        if prev_node is None:
            return

        new_node = Node(new_data)

        # Set new node's next as prev node's next
        new_node.set_next(prev_node.get_next())

        # Make next of prev node to new node
        prev_node.set_next(new_node)

        # Make prev of new node to previous node
        new_node.set_prev(prev_node)

        # Change previous of new_node's next node
        if new_node.get_next() is not None:
            new_node.get_next().set_prev(new_node)

    def append(self, new_data):
        """
        Given a reference to the head of DLL and integer,
        appends a new node at the end
        """
        new_node = Node(new_data)

        # If linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while last.get_next() is not None:
            last = last.get_next()

        # Change the next of the last node
        last.set_next(new_node)

        # Make last node as previous of new node
        new_node.set_prev(last)

        print(new_node)
        return new_node

    def delete_node(self, delete):
        if self.head is None or delete is None:
            return

        if self.head == delete:
            self.head = delete.get_next()

        # Change next only if node to be deleted in NOT the last node
        if delete.get_next() is not None:
            delete.get_next().set_prev(delete.get_prev())

        # Change prev only if node to be deleted is Not the first node
        if delete.get_prev() is not None:
            delete.get_prev().set_next(delete.get_next())

        # Finally free the memory occupied by delete
        # Call python garbage collector
        gc.collect()

    def print_list(self):
        """
        Prints content of linked list starting from the given node
        """
        if self.head is None:
            return
        this_node = self.head

        print("None", end='')
        while this_node is not None:
            print("<-{}->".format(this_node.get_data()), end='')
            this_node = this_node.get_next()

        print("None")

def main():
    mylist = DLinkedList()
    mylist.append(7)
    mylist.push(6)
    mylist.push(1)
    node4 = mylist.append(4)
    print("Node 4 location is :".format(type(node4)))
    mylist.insert_after(mylist.get_head().get_next(), 8)
    print("\nCreated DLL is:")
    mylist.print_list()

    print("\nAfter the deleting the node 6")
    mylist.delete_node(mylist.get_head().get_next())
    mylist.print_list()

    print("\nAfter deleting node 4")
    mylist.delete_node(node4)
    mylist.print_list()

if __name__ == '__main__':
    main()


