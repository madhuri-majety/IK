"""

Zip Given Linked List From Ends


Problem Statement:

Given an integer singly linked list, zip it from its two ends. (Looking at the sample test case will make it more clear.)

You have to do it in-place i.e. in the same linked list, with using only constant extra space.

Input Format:

There is only one argument in input, denoting integer singly linked list.

Output Format:

Return zipped linked list.

Constraints:

0 <= size of linked list <= 100000
-2 * 10^9 <= value stored in any node <= 2 * 10^9

Sample Test Case:

Sample Input:

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

Sample Output:

1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL

(Other modification to try yourself for practice: zip two separate lists and unzip them back into original lists. i.e. unzip(zip(L1, L2)) should return L1 and L2.)


Approach:
- The task is to achieve desired linked list using O(1) space
- Split the list from the middle into two lists. We are splitting the list into two and not creating a new linked list
  hence maintaining O(1) space.
- Now we have two list list1 & list2
- Reverse the second list - list2
- Now merge the lists picking one node from each list
"""

from IK.LinkedLists.singly_linked_list import LinkedList

def reverse_linked_list(curr):
    prev = None
    next = None
    while curr:
        next = curr.get_next()
        curr.set_next(prev)
        prev = curr
        curr = next

    return prev

def zip_given_linked_list(llist):
    if llist.get_head() is None:
        return
    head = llist.get_head()
    slow = llist.get_head()
    fast = llist.get_head()

    # Find the middle of the linked list using slow & fast pointers
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()
        fast = fast.get_next().get_next()

    # Separate linked lists from middle
    list1 = head
    list2 = slow.get_next()

    # Now break main linked list into two lists
    slow.set_next(None)

    # Now reverse the second linked list - list2
    list2 = reverse_linked_list(list2)

    while(list2):
        next1 = list1.get_next()
        next2 = list2.get_next()
        list1.set_next(list2)
        list2.set_next(next1)
        list1 = next1
        list2 = next2



def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print("Linked List before zipping")
    ll.print_list()

    print("Linked List after zipping")
    zip_given_linked_list(ll)
    ll.print_list()

if __name__ == '__main__':
    main()