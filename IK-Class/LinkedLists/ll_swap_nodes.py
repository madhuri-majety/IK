"""
Swap nodes in a single linked list
The idea it to first search x and y in given linked list.
If any of them is not present, then return. While searching for x and y,
keep track of current and previous pointers. First change next of previous pointers,
then change next of current pointers.
"""

from singly_linked_list import LinkedList, Node

def swap_nodes(llist, x, y):
    if x == y:
        return

    # Search for x and keep track of prev node & current node
    prevX = None
    currX = llist.get_head()
    while currX is not None and currX.data != x:
        prevX = currX
        currX = currX.get_next()

    # Search for y and keep track of prev node & current node
    prevY = None
    currY = llist.get_head()
    while currY is not None and currY.data != y:
        prevY = currY
        currY = currY.get_next()

    # If either x or y not present then return
    if currX is None or currY is None:
        return

    # First connect the next of previous nodes
    if prevX is not None:
        prevX.set_next(currY)
    else:
        llist.set_head(currY)


    if prevY is not None:
        prevY.set_next(currX)
    else:
        llist.set_head(currX)

    # Second connect the next of current nodes
    temp = currX.get_next()
    currX.set_next(currY.get_next())
    currY.set_next(temp)

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List:")
llist.print_list()

swap_nodes(llist, 2, 1)
llist.print_list()

swap_nodes(llist,8,1)
llist.print_list()

swap_nodes(llist,2,7)
llist.print_list()



"""
llist.delete_node_pos(4)
print("\nLinked List after Deletion at position 4: ")
llist.print_list()
llist.delete_node(3)
print("\nLinked List after Deletion of node 3: ")
llist.print_list()
"""



