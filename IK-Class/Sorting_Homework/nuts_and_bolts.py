import random

"""
Match the Nuts and bolts of equal size. The number of nuts and bolts are same.
Example Input:
Nuts = [N3, N2, N1, N4]
Bolts = [B4, B2, B3, B1]

Output:
N1B1
N2B2
N3B3
N4B4
"""

def partition(arr, st, end):
    pivot = arr[end]
    pindex = st

    for i in range(st,end):
        if arr[i] <= pivot:
            arr[pindex], arr[i] = arr[i], arr[pindex]
            pindex += 1
    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex

def randomized_partition(arr, st, end):
    idx = random.randint(st, end)
    arr[idx], arr[end] = arr[end], arr[idx]
    return partition(arr,st,end)

def qsort(arr, st, end):
    if st <= end:
        pi = randomized_partition(arr, st, end)

        qsort(arr, st, pi-1)
        qsort(arr, pi+1, end)


def main():
    nuts = ['N3', 'N2', 'N1', 'N4']
    bolts = ['B4', 'B2', 'B3', 'B1']

    qsort(nuts, 0, len(nuts)-1)
    print(nuts)
    qsort(bolts, 0, len(bolts)-1)
    print(bolts)

    for i in range(len(nuts)):
        print("{}{}".format(nuts[i],bolts[i]))

if __name__ == '__main__':
    main()

