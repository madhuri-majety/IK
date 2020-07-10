"""
A python module that implements singly linked list
"""

class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

class LinkedList(object):
    def __init__(self, h = None):
        self.head = h
        self.size = 0

    def get_head(self):
        return self.head

    def set_head(self, h):
        self.head = h

    def get_size(self):
        return self.size

    def push(self, data):
        """
        Push adds the node to the beginning of the list
        """
        # Create new node with given data
        new_node = Node(data)

        # New node next pointer points to head of linked list
        new_node.set_next(self.head)

        # Move the head to the new node
        self.head = new_node

        # Increment the size
        self.size += 1

    def insert(self, prev_node, data):
        """
        Insert data after the prev node
        """
        # Create the node for the given data
        new_node = Node(data)

        # Point the new node next to prev node next
        # and prev node next to new node
        if prev_node:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)

        # Increment the size
        self.size += 1

    def append(self, data):
        """
        Append the data to the end of the list
        """
        # Create a node
        new_node = Node(data)

        # If the head is null, add this element as head
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        last = self.head

        while last.get_next() is not None:
            last = last.get_next()

        last.set_next(new_node)
        self.size += 1

    def delete_node(self,key):
        this_node = self.head
        prev_node = None

        if this_node is None:
            return

        while this_node:
            if this_node.get_data() == key:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False

    def delete_node_pos(self,pos):
        if self.head is None:
            return

        this_node = self.head

        if pos == 0:
            self.head = this_node.get_next()
            this_node = None
            self.size -= 1
            return

        for i in range(pos-1):
            this_node = this_node.get_next()
            if this_node is None:
                break

        if this_node is None:
            return
        if this_node.get_next() is None:
            return

        next = this_node.get_next()
        next = next.get_next()

        this_node.set_next(next)

    def find(self, data):
        this_node = self.head

        while this_node:
            if this_node.get_data() == data:
                return True
        return False

    def get_nth_node(self, index):
        curr = self.head
        count = 0

        while curr:
            if count == index:
                return curr.get_data()
            else:
                count += 1
                curr = curr.get_next()
        return None

    def print_list(self):
        print("Printing List...")
        this_node = self.head

        while this_node:
            print("{}->".format(this_node.get_data()), end='')
            this_node = this_node.get_next()

        print("NULL")

"""
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
llist.print_list()

print(llist.get_nth_node(3))

print("Created Linked List:")
llist.print_list()
llist.delete_node_pos(4)
print("\nLinked List after Deletion at position 4: ")
llist.print_list()
llist.delete_node(3)
print("\nLinked List after Deletion of node 3: ")
llist.print_list()

"""


