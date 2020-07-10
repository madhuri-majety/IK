"""
Retain Best Cache:
* Get(k) -> v in O(1)
* If <k,v> is not present in cache, pull from data source
* If cache is full, evict lowest ranked <k,v> from the cache
* Use get_rank(v) => api

Notes:
* Optimal solution:
    * Primary DS - Hashmap
    * Auxillary DS - BST for ranks, linked list to keys
        * Why BST compared to Minheap?
            * When a k,v is pulled from data store and it has to be stored in auxiliary data structure and
              if there are duplicate ranks, the rank has to searched in auxiliary DS to append it to its linked list.
                * Searching for rank in BST is O(logN)
                * Min heap is good but searching for a random rank takes O(N) as min heap is a binary tree
* How is this diffferent from LRU Cache
    * In LRU cache, you unconditionally evict the least recently used and add new value.
    * In retain best cache problem, compare the rank first and find the right place and then put it in as ranks can be repetitive.

"""