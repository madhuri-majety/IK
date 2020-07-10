#! /usr/lib/python3

def binary_search_first_occ(list,value):
    low = 0
    high = len(list)-1
    result = None
    while(low <= high):
        mid = low + (high-low)//2
        if list[mid] == value:
            result = mid
            high = mid-1
        elif value < list[mid]:
            high = mid-1
        else:
            low = mid+1
    return result

list = [2,4,10,10,10,18,20]
input = input("Enter the number to search in between 1 to 20 - ")
print("Number to search is {}".format(input))
result = binary_search_first_occ(list,int(input))
if (result is not None):
    print("Element found at index {}".format(result))
else:
    print("Element not found")
