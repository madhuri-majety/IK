"""
Given a linked list, check if the the linked list has loop or not. Below diagram shows a linked list with a loop.

Approach 1: (Hashing)
Traverse the list one by one and keep putting the node addresses in a Hash Table.
At any point, if NULL is reached then return false and if next of current node points to any of the previously
stored nodes in Hash then return true.
O(N) time and O(N) extra space.

Approach 2: Mark Visited nodes
This solution requires modifications to basic linked list data structure.  Have a visited flag with each node.
Traverse the linked list and keep marking visited nodes.  If you see a visited node again then there is a loop.
This solution works in O(n) but requires additional information with each node.
O(N) time and O(N) extra space.


Approach 3: (Floyd's loop detection algorithm)  ***********
This is the fastest method. Traverse linked list using two pointers.
Move one pointer to one and another pointer twice . If pointers meet at same node then there is a loop.
If pointers dont meet then there is no loop.
"""
from singly_linked_list import LinkedList, Node

def detect_loop_hash(llist):
    s = set()

    temp = llist.get_head()

    while temp:
        if temp in s:
            return True
        s.add(temp)

        temp = temp.get_next()

    return False

def detect_loop_floyds(llist):
    slow_ptr = llist.get_head()
    fast_ptr = llist.get_head()

    while slow_ptr is not None and fast_ptr is not None and fast_ptr.get_next() is not None:
        slow_ptr = slow_ptr.get_next()
        fast_ptr = fast_ptr.get_next()
        fast_ptr = fast_ptr.get_next()
        if slow_ptr == fast_ptr:
            return True

    return False

def count_nodes(ptr):
    res = 1
    temp = ptr
    while temp.get_next() != ptr:
        res += 1
        temp = temp.get_next()

    return res

def count_nodes_in_loop(llist):
    slow_p = llist.get_head()
    fast_p = llist.get_head()
    while(slow_p and fast_p and fast_p.get_next()):
        slow_p = slow_p.get_next()
        fast_p = fast_p.get_next().get_next()
        if slow_p == fast_p:
            return count_nodes(slow_p)

    return 0

def main():
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    # Create a loop for testing
    llist.head.next.next.next.next = llist.head

    if (detect_loop_hash(llist)):
        print("Loop found")
    else:
        print("No Loop ")

    if (detect_loop_floyds(llist)):
        print("Loop found")
    else:
        print("No Loop ")

    print(count_nodes_in_loop(llist))


if __name__ == '__main__':
    main()