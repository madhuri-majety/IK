"""
Merge sort is a divide and conquer algorithm. It divides input array into two halves, calls itself for the two halves
and then merges the two sorted halves.
- Divide & Conquer algorithm
- Recursive
- Stable algorithm
- Space - O(N)
- Time Complexity - O(NlogN)
"""

def merge_sort(a, st, en):
    if st < en:
        mid = st + (en-st)//2

        merge_sort(a, st, mid)
        merge_sort(a, mid+1, en)
        merge(a, st, mid, en)

def merge(a, st, mid, en):
    nl = mid - st + 1
    nr = en - mid

    l = [0] * nl
    r = [0] * nr

    for i in range(0, nl):
        l[i] = a[st+i]

    for i in range(0, nr):
        r[i] = a[mid + 1 + i]

    i, j, k = 0, 0, st

    while i < nl and j < nr:
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
            k += 1
        else:
            a[k] = r[j]
            j += 1
            k += 1

    while i < nl:
        a[k] = l[i]
        i += 1
        k += 1

    while j < nr:
        a[k] = r[j]
        j += 1
        k += 1


def main():
    list = [1, 4, 7, 21, 2, 3, 5, 6]
    print("Before sorting the list: ", list)
    merge_sort(list, 0, len(list) - 1)
    print("After merge sorting the list: ", list)

if __name__ == '__main__':
    main()
