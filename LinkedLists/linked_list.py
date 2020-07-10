"""
Class for Linked list operations
"""

class Node(object):
    def __init__(self,data,n = None):
        self.data = data
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()

                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False

    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                self.root = this_node.get_next()

        return None

    def printList(self):
        temp = self.root

        while temp:
            print(temp.data)
            temp = temp.next_node

if __name__ == '__main__':
    myList = LinkedList()
    myList.add(5)
    myList.add(8)
    myList.add(12)
    myList.printList()
