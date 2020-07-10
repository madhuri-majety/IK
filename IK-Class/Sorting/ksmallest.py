"""
Find K smallest elements in the stream of input

*********** Crux: Use Max heap to find the K smallest


1. Take k elements and build a max heap. Time Complexity is O(K)
2. Starting from k index to n-1 index, compare the value at that index to root of the max heap and if value is less than
root, then replace the root with smallest element and heapify it. Time Complexity is (n-k)*logK ((n-k) because the
heapify is done only for n-k elements)
3. By end of the iteration, we will have k smallest elements in the list

Time Complexity: O(k+ (n-k)logK)
Space Complexity: O(K)
"""

def max_heapify(arr, size, index):
    largest = index
    left = (2*index)+1
    right = (2*index)+2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, size, largest)

def ksmallest_maxheap(arr, k):
    n = len(arr)

    h = []
    for i in range(k):
        h.append(arr[i])

    for i in range(len(h)//2 -1, -1, -1):
        max_heapify(h, len(h), i)

    for i in range(k, n):
        if arr[i] < h[0]:
            h[0] = arr[i]
            max_heapify(h, len(h), 0)

    return h

def main():
    k = int(input("Enter the value of k:"))
    list = [10, 4, 3, 2, 11, 15, 1, 16]

    print("K Smallest elements are :", ksmallest_maxheap(list, k))


if __name__ == '__main__':
    main()