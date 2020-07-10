"""
Linked List Implementation:
* Even for Linked list, instead of maintaining one pointer ‘head’
that points to the starting of the list, lets have two pointers,
front(head) and rear(tail) and for every operation both front and rear
will be updated. That way we can keep operation as O(1) complexity

Pseudo Code:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        temp  = Node(data)
        if (self.front == None and self.rear == None):
            self.front = self.rear = temp

        self.rear->next = temp
        self.rear = temp

    def dequeue():
        temp = self.front
        if (self.front == None):
            return None
        elif (self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

    def front(self):
        return self.front.data

    def isempty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False




"""
