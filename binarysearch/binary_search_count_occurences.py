#! /usr/bin/python3

def binary_search(list, value, first_occ):
    low = 0
    high = len(list) - 1
    result = None
    while(low <= high):
        mid = low + (high-low)//2
        if value == list[mid]:
            result = mid
            if first_occ:
                high = mid - 1
            else:
                low = mid + 1
        elif value <= list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result

list = [1,1,3,3,5,5,5,5,5,9,9,9,11]
print("printing list:\n {}".format(list))
input = input("Enter the number to find the occurences - ")
print("Number to find the number of occurences is {}".format(input))

first_index = binary_search(list, int(input), True)
if first_index is not None:
    last_index = binary_search(list, int(input), False)
    print("Count of {} is {}".format(input, last_index-first_index+1))
else:
    print("Element {} is  not found".format(input))
