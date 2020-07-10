"""
Merge first sorted array into second sorted array
arr1 - size n
arr2 - size 2n
"""

def find_empty_index(arr):
    idx = -1
    for i, value in enumerate(arr):
        if value == None:
            idx = i
            break
    return idx

def merge(a, b):
    n1 = len(a)
    n2 = len(b)

    if n1 > n2:
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a

    i = len(smallest)-1
    print(i)
    j = find_empty_index(largest)-1
    print(j)
    k = len(largest)-1
    print(k)

    if k == j+i+1:
        print("Enough space to merge the arrays")
    else:
        print("Not enough space to merge the arrays")
        return None

    while i >= 0 and j >= 0:
        if smallest[i] > largest[j]:
            largest[k] = smallest[i]
            k = k-1
            i = i-1
        elif smallest[i] < largest[j]:
            largest[k] = largest[j]
            k = k-1
            j = j-1
        else:
            largest[k] = largest[j]
            k = k-1
            j = j-1
            largest[k] = smallest[i]
            k = k-1
            i = i-1

    while i >= 0 and k >= 0:
        largest[k] = smallest[i]
        k = k - 1
        j = j - 1

    while j >= 0 and k >= 0:
        largest[k] = largest[j]
        k = k-1
        j = j-1


    return largest

def main():
    arr1 = [1,3,5,7,9]
    arr2 = [1,3,5,7,9,None,None,None,None,None]

    print("Merged array is", merge(arr1, arr2))

if __name__ == '__main__':
    main()


