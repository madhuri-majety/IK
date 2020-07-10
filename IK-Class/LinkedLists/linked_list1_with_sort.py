"""
Implement Linked list with sort() function
"""

class Node(object):
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def to_string(self):
        return "Node Value: {} ".format(str(self.data))

    def has_next(self):
        if self.get_next() is None:
            return False
        return True


class LinkedList(object):
    def __init__(self, h = None):
        self.head = h
        self.size = 0

    def push(self, data):
        """
        Adding element at the beginning of the list
        :param data:
        :return:
        """
        new_node = Node(data,self.head)
        self.head = new_node
        self.size += 1

    def insert(self, prev_node, data):
        new_node = Node(data)

        if prev_node:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)

    def append(self,data):
        """
        Add element at the end of the list
        :return:
        """
        new_node = Node(data)
        last = self.head

        if self.head is None:
            self.head = new_node
            return

        while last.has_next():
            last = last.get_next()

        last.set_next(new_node)


    def remove_node(self, data):
        this_node = self.head
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
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

    def get_size(self):
        return self.size

    def find(self, d):
        this_node = self.head

        while this_node:
            if this_node.get_data() == d:
                return True
            else:
                this_node = this_node.get_next()

        return False

    def print_list(self):
        print("Printing List...")
        if self.head is None:
            return
        curr_item = self.head
        print(curr_item.to_string())
        while curr_item.has_next():
            curr_item = curr_item.get_next()
            print(curr_item.to_string())

    def sort(self):
        if self.size > 1:
            new_list = []
            curr = self.head
            new_list.append(curr)
            while curr.has_next():
                curr = curr.get_next()
                new_list.append(curr)
            new_list = sorted(new_list, key = lambda node: node.get_data(), reverse = True)
            new_ll = LinkedList()
            for node in new_list:
                new_ll.push(node.get_data())

            return new_ll
        return self



myList = LinkedList()
myList.push(5)
myList.push(9)
myList.push(3)
myList.push(8)
myList.push(9)
print("size= "+str(myList.get_size()))
myList.print_list()
myList = myList.sort()
myList.print_list()
myList.remove_node(8)
print("size= "+str(myList.get_size()))
print(myList.remove_node(12))
print("size= "+str(myList.get_size()))






