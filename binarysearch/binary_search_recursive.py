#! /usr/bib/python
import time

def binary_search_rec(list, low, high, elem_to_find):
    if low <= high:
        mid = low + (high-low)//2
        print("Printing mid {}". format(mid))
        if list[mid] == elem_to_find:
            return mid
        elif elem_to_find < list[mid]:
            return binary_search_rec(list, low, mid-1, elem_to_find)
        else:
            return binary_search_rec(list, mid+1, high, elem_to_find)

    else:
        return -1

input = int(input("Enter the number to search:"))
print("Number to search is {}". format(input) )
#list = [1,2,3,4,5,6,7,8,9]
list = [x for x in range(1,101)]
start_time = time.time()
result = binary_search_rec(list, 0, len(list)-1, input)
end_time = time.time()
print("Index is {}". format(result))
if (result>=0):
    print("Found the element")
else:
    print("Not found the element")
print("Time took to search is {}". format(end_time - start_time))
