"""
Swap kth Nodes In Given Linked List

https://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/

Problem Statement:

Given an integer singly linked list of size n,
you have to swap kth (1-indexed) node from the beginning, with kth node from the end.
You have to swap the nodes themselves, not just the contents.

Input Format:

There are two arguments in input. First is an integer singly linked list and second is an integer k.

Output Format:

Return linked list after swapping kth nodes.

Constraints:

1 <= n <= 100000
-2 * 10^9 <= value stored in any node <= 2 * 10^9
1 <= k <= n
Try to access linked list nodes minimum number of times.

Sample Test Case:

Sample Input:

list: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL
k: 2

Sample Output:

1 -> 7 -> 3 -> 4 -> 2 -> 0 -> NULL

"""

from IK.LinkedLists.singly_linked_list import LinkedList

def swapkthnodes(llist, k):
    if llist is None:
        return

    size = llist.get_size()

    # Check if k is valid
    if size < k:
        return

    # If x(kth node from beginning) and y(kth node from end or n-k+1 from beginning) are the same then return

    if 2*k - 1 == size:
        return

    # Find kth node from the beginning of the list. We also find previous of kth node
    # because we need to update next pointer of previous
    currX = llist.get_head()
    prevX = None

    for i in range(1,k):
        prevX = currX
        currX = currX.get_next()


    # Similarly find the kth node from the end of the list. we also find previous of that node
    currY = llist.get_head()
    prevY = None
    for i in range(1, size-k+1):
        prevY = currY
        currY = currY.get_next()

    # If either x or y not present then return
    if currX is None or currY is None:
        return

    # First connect the next of previous nodes
    if prevX is not None:
        prevX.set_next(currY)

    if prevY is not None:
        prevY.set_next(currX)


    # Update the curr nodes next pointers
    temp = currX.get_next()
    currX.set_next(currY.get_next())
    currY.set_next(temp)

    if k == 1:
        llist.set_head(currY)

    if k == size:
        llist.set_head(currX)


llist = LinkedList()
llist.push(0)
llist.push(7)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Created Linked List:")
llist.print_list()
k = 3
swapkthnodes(llist, k)

print("After swapping {}th elements:".format(k))
llist.print_list()





