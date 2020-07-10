"""
Reverse Given Linked List In Groups Of k

https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

Problem Statement:

Given an integer singly linked list of size n and an integer k, you have to reverse every k nodes of the linked list.

There are two cases possible:

1) When n % k = 0: There will be n / k  groups of size k. So, you have to reverse n / k  groups of size k.

2) When n % k != 0: There will be floor(n / k) groups of size k and one group of size n % k. So, you have to reverse floor(n / k) groups of size k and one group of size n % k.

(Looking at sample test cases will make it more clear.)

Input Format:

There are two arguments in input. First is an integer singly linked list and second is an integer k.

Output Format:

Return linked list after reversing it in groups of k.

Constraints:

1 <= n <= 100000
-2 * 10^9 <= value stored in any node <= 2 * 10^9
1 <= k <= n
Solve it with constant extra space.

Sample Test Case:

Sample Input 1:

list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
k: 3

Sample Output 1:

3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL

Explanation 1:

n = 6, k = 3 hence n % k = 0. So there are n / k = 6 / 3 = 2 groups of size k = 3.

Groups to be reversed are (1 -> 2 -> 3) and (4 -> 5 -> 6).

Sample Input 2:

list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
k: 3

Sample Output 2:

3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7-> NULL

Explanation 2:

n = 8, k = 3 hence n % k != 0, so there are floor(n / k) = floor(8 / 3) =
2 groups of size k = 3 and one group of size n % k = 8 % 3 = 2.

Groups to be reversed are (1 -> 2 -> 3), (4 -> 5 -> 6) and (7 -> 8).
"""

from IK.LinkedLists.singly_linked_list import LinkedList

def reverse_in_groups(head, k):
    curr = head
    next = None
    prev = None
    count = 0

    while curr and count < k:
        next = curr.get_next()
        curr.set_next(prev)
        prev = curr
        curr = next
        count += 1

    # next is a pointer to k+1 the node
    # Recursively call for the list starting from current
    # Make rest of the list as next of first node
    if next is not None:
        head.set_next(reverse_in_groups(next, k))


    # prev is new head of the input list
    return prev


# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.print_list()
head = llist.get_head()
print(head.get_data())
llist.set_head(reverse_in_groups(head, 3))

print("\nReversed Linked list")
llist.print_list()
