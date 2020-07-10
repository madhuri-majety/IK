"""
Given a stream of characters, find the first non-repeating character from stream.
You need to tell the first non-repeating character in O(1) time at any moment.

Solution:
Design:
As the expected run time in O(1) we need to maintain auxillary data structure.
Main DS = Hash
Auxillary DS = Doubly Linked List

The idea is to use a DLL (Doubly Linked List) to efficiently get the first non-repeating character from a stream.
The DLL contains all non-repeating characters in order, i.e., the head of DLL contains first non-repeating character,
the second node contains the second non-repeating and so on.

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
            return self.head

        # Else traverse till the last node
        last = self.head
        while last.get_next() is not None:
            last = last.get_next()

        # Change the next of the last node
        last.set_next(new_node)

        # Make last node as previous of new node
        new_node.set_prev(last)

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

class NonRepeatingChar(object):
    def __init__(self, data_str):
        self.data_str = data_str
        self.dll = DLinkedList()
        self.hash = {}

    def parse_stream(self):
        for i, char in enumerate(self.data_str):
            if char not in self.hash:
                self.hash[char] = {}
                self.hash[char]['index'] = i
                self.hash[char]['count'] = 1
                self.hash[char]['dll_pos'] = self.dll.append(char)
            else:
                dll_pos = self.hash[char]['dll_pos']
                self.dll.delete_node(dll_pos)

                self.hash[char]['count'] = self.hash[char]['count'] + 1
                self.hash[char]['index'] = i
                self.hash[char]['dll_pos'] = None

        print("DEBUG: Printing hash: {}".format(self.hash))
        print("DEBUG: Printing DLL: ", end=' ')
        self.dll.print_list()


    def get_first_non_repeating_char(self):
        return self.dll.get_head().get_data()

def main():
    print("Stream : GeeksforGeeks")
    npc1 = NonRepeatingChar("GeeksforGeeks")
    npc1.parse_stream()
    print(npc1.get_first_non_repeating_char())


    print("\n\nStream: GeeksQuiz")
    npc2 = NonRepeatingChar("GeeksQuiz")
    npc2.parse_stream()
    print(npc2.get_first_non_repeating_char())

if __name__ == '__main__':
    main()



