
"""
Build method implementation from heapq for merging k sorted lists
https://hg.python.org/cpython/file/default/Lib/heapq.py#l314

 list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))

    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

If *key* is not None, applies a key function to each element to determine

    its sort order.


list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))

    ['dog', 'cat', 'fish', 'horse', 'kangaroo']
"""
from heapq import merge
import heapq


def merge_sorted_arrays(arrays):
    desc = 0
    for i in arrays:
        if len(i) >= 2 and i[0] > i[1]:
            desc = 1
            i.sort()
    if desc:
        return sorted((list(merge(*arrays))), reverse=True)
    else:
        return list(merge(*arrays))

def mergearrays_heap(iarray):
    h = []
    result = []

    # Initialize heap with first element from all the arrays, its item index and array index
    # into a tuple and push it to heap
    for i, v in enumerate(iarray):
        heapq.heappush(h, (v[0], 0, i))

    while h:
        #print(h)
        curr_min_tuple = heapq.heappop(h)
        curr_item, curr_item_index, curr_arr_idx = curr_min_tuple
        result.append(curr_item)
        if curr_item_index < len(iarray[curr_arr_idx]) -1:
            heapq.heappush(h, (iarray[curr_arr_idx][curr_item_index+1], curr_item_index+1, curr_arr_idx))

    return result


def main():
    """
    _iarray_rows = 0
    _iarray_columns = 0
    _iarray_rows = int(input())
    _iarray_columns = int(input())

    _iarray = []
    for _iarray_i in range(_iarray_rows):
        _iarray_temp = [int(_iarray_t) for _iarray_t in input().strip().split(' ')]
        _iarray.append(_iarray_temp)

    res = merge_sorted_arrays(_iarray)
    print(res)

    """
    _iarray = [[2,6,8,10], [1,3,5,7,9], [0,11,21]]
    res = mergearrays_heap(_iarray)
    print(res)

    _iarray2 = [[2,6,8,10], [1,3,5,7,9], [0,11,21]]
    new = list(heapq.merge(_iarray2))
    print("Using Heapq merge method: {}".format(new))


if __name__ == '__main__':
    main()
