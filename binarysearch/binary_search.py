#! /usr/bin/python3
import time

def binary_search(list, input):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = start + (end - start) // 2
        print("Printing mid {}". format(mid))
        if list[mid] == input:
            return mid
        elif input < list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


input = int(input("Enter the number to search:"))
print("Number to search is {}". format(input) )
#list = [1,2,3,4,5,6,7,8,9,]
list = [x for x in range(1, 100)]
start_time = time.time()
result = binary_search(list, input)
end_time = time.time()

print("Index is {}". format(result))
if( result >= 0 ):
    print("Found the element")
else:
    print("Not found the element")
print("Time took to search is {}". format(end_time - start_time))
