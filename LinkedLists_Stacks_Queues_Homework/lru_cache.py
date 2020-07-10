"""
https://www.geeksforgeeks.org/lru-cache-implementation/
https://leetcode.com/problems/lru-cache/description/

Design And Implement LRU Cache


Problem Statement:

The LRU caching scheme removes the least recently used frame, when the cache is full and a new page is referenced
which is not there in the cache.

You are given one integer named capacity, denoting the maximum size possible of the LRU cache.
Also you are given three integer arrays named query_type, key and value, each having size n.

query_type[i], key[i] and value[i] together denotes one query. So there are total n queries.

query_type contains only 0 or 1. query_type[i] = 0 means ith query is GET query and query_type[i] = 1
means ith query is SET query. key and value arrays contain only positive integers.

You have to return array containing answers for GET queries.

GET query:

For GET query only key[i] matters, do not care what is stored in value[i].

For each GET query append one integer in the array to be returned.
Append the value of the key[i], if the key[i] exists in the cache, otherwise append -1.

SET query:

If key[i] is already present in the cache then update its value to value[i],
else add key[i] with value value[i] in the cache.

Input Format:

There are four arguments in the input. First is integer named capacity.
Second is integer array named query_type. Third is integer array named key. Fourth is integer array named value.

Output Format:

Return an array containing answers for GET queries.

Constraints:

1 <= n <= 10^5
1 <= capacity <= 10^5
0 <= query_type[i] <= 1
1 <= key[i] <= 10^5
1 <= value[i] <= 10^5

Sample Test Case:

Sample Input:

capacity = 2

index  	  query_type  	  key  	  value
0          	  1            5      	11
1          	  1            10      	22
2          	  0            5        11
3          	  1            15      	33
4          	  0            10       -1
5          	  1            5      	55
6          	  0            5         1

(
this is same as:
query_type = [1 1 0 1 0 1 0]
key =   [5 10 5 15 10 5 5]
value = [11 22 1 33 1 55 1]
)

Sample Output:

[11 -1 55]

Explanation:

Initially cache is empty.

Step 1:
SET: 5 -> 11
Noe cache contains (5 ->11).

Step 2:
SET: 10 -> 22
Now cache contains (5 -> 11) and (10 -> 22).

Step 3:
GET: 5
Cache contains (5 ->11), so append 11 to answer.

Step 4:
SET: 15 -> 33
Now cache contains (5 -> 11) and (15 -> 33).
Note that here (10 -> 22) is removed because 10 is the least recently used. 5 was used in the previous query!

Step 5:
GET: 10
Cache does not contain key 10 (it was removed in previous step), so append -1 to answer.

Step 6:
SET: 5 -> 55
Now cache contains (5 -> 55) and (15 -> 33). Note that (5 -> 11) is updated to (5 -> 55).

Step 7:
GET: 5
Cache contains (5 -> 55), so append 55 to answer.

Approach:
We use two data structures to implement the cache
1. Doubly linked list (Queue implemented using doubly linked list)
    - Linked list nodes contain a tuple of (key, value)
    - Linked list should have both head and tail
    - Recently accessed element is always at the head
    - Least recently used (based on time) is at the tail of the linked list
    - Tail pointer is useful in eviction process when the key doesn't exist in cache and fetched from datastore
2. Hashmap
    - Hashmap is used to get the value of a key in O(1) time complexity
    - Hashmap stores the key and a reference to the node in linked list (not the value)
    - When the middle of the linked list has to be moved to the head, the hash map references doesn't have to get
    updated as the node reference wont change just the prev and next pointers and head in linked list has to be updated.

"""

import gc

class ListNode(object):
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_key(self, k):
        self.key = k

    def set_value(self, v):
        self.value = v

    def set_next(self, n):
        self.next = n

    def set_prev(self, p):
        self.prev = p


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cachemap = dict()


    def erase_node(self, node):
        """
        Given a node in linkedlist, remove the node from the linked list
        """
        prev_node = node.get_prev()
        next_node = node.get_next()

        if prev_node is not None:
            prev_node.set_next(next_node)

        if next_node is not None:
            next_node.set_prev(prev_node)

        # If node to be removed in the only node in linked list, set head and tail
        if self.head == self.tail:
            self.head = self.tail = None

        # If node to be removed in head, set head
        if self.head == node:
            self.head = next_node

        # If node to be removed in tail, set tail
        if self.tail == node:
            self.tail = prev_node

        gc.collect()

    def dll_add_to_front(self, key, value):
        """
        Given a key, value add this list node to front of the linked list
        """
        new_lnode = ListNode(key, value)
        if self.head is None:
            self.head = new_lnode
            self.tail = new_lnode

        else:
            new_lnode.set_next(self.head)
            self.head.set_prev(new_lnode)
            self.head = new_lnode

        self.cachemap[key] = self.head

    def evict_least_recently_used(self):
        key_to_evict = self.tail.get_key()
        del self.cachemap[key_to_evict]

        # If only one node, set head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        # Set tail
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

        gc.collect()

    def get(self, key):
        """
        Return value of the key, if key is present, else return -1
        If key present, then update the key position in the linked list to head
        """
        if key not in self.cachemap:
            return -1

        value = self.cachemap[key].get_value()

        # Remove (key,value) node from the original position
        self.erase_node(self.cachemap[key])

        # Add this (key,value) to the front of the list
        self.dll_add_to_front(key, value)
        return value

    def set(self, key, value):
        """
        If key is present in cache then update its value, else add {key, value} pair in cache
        """
        if key in self.cachemap:
            self.erase_node(self.cachemap[key])
            self.dll_add_to_front(key, value)

        else:
            if len(self.cachemap) == self.capacity:
                self.evict_least_recently_used()
            else:
                self.dll_add_to_front(key, value)

    def print_cachemap(self):
        print(self.cachemap)

    def print_dll(self):
        if self.head is None:
            return

        curr = self.head
        print("None", end='')
        while curr is not None:
            print("<-({},{})->".format(curr.get_key(), curr.get_value()), end='')
            curr = curr.get_next()

        print("None")


def lru_cache_util(capacity, qtype, keys, values):
    cache = LRUCache(capacity)
    res = []
    for i, type in enumerate(qtype):
        if type == 0:
            res.append(cache.get(keys[i]))
            cache.print_cachemap()
            cache.print_dll()
        else:
            cache.set(keys[i], values[i])
            cache.print_cachemap()
            cache.print_dll()

    return res

def main():
    capacity = 2
    query_type = [1, 1, 0, 1, 0, 1, 0]
    keys = [5, 10, 5, 15, 10, 5, 5]
    values = [11, 22, 1, 33, 1, 55, 1]

    print(lru_cache_util(capacity, query_type, keys, values))

if __name__ == '__main__':
    main()
