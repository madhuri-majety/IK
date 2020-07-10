"""
Maintain two pointers, front and rear in an array
Enqueue: Always add elements from rear
Dequeue: Increment front pointer

Psuedo code:
class QueueArray(arr):
    def init(self):
        self.front = -1 (Starting Index)
        self.rear = -1 (Starting Index)
        self.arr = arr

    def isempty(self):
        if self.rear == -1 and self.front == -1:
            return True
        return False

    def enqueue(self,x):
        if (self.rear+1) % N == self.front:
            raise exception
        elif isempty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1) % N

        self.arr[self.rear] = x

    def dequeue():
        if self.isempty():
            return
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % N

    def front(self):
        return self.arr[self.front]

"""