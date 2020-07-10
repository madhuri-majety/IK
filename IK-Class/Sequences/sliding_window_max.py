"""
Maximum in sliding window

An integer array named arr is given to you. Size of arr is n and assume it is very large.
There is sliding window of size w which is moving from the very left of the array to the very right. You can also
see the w numbers in the window. Each time the sliding window moves rightwards by one position.
you have to find the max number in the window each time.

Input:
There are two arguments in the input. First is an integer array arr. Second is the window width w.

Method1:
Run two loops. In the outer loop, take all subarrays of size k. In the inner loop, get the max of the current subarray.
Time Complexity: O(NK)


Optimal Solution - Dequeue of size k
How one could improve the time complexity? The first idea is to use a heap, since in a maximum heap heap[0]
is always the largest element. Though to add an element in a heap of size k costs log⁡(k),
that means O(N log⁡(k) time complexity for the solution.

    Could we figure out O(N)solution?

Let's use a deque (double-ended queue), the structure which pops from / pushes to either side with the same O(1) performance.

It's more handy to store in the deque indexes instead of elements since both are used during an array parsing.

Algorithm

The algorithm is quite straigthforward :

    Process the first k elements separately to initiate the deque.

    Iterate over the array. At each step :

        Clean the deque :

            Keep only the indexes of elements from the current sliding window.

            Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.

        Append the current element to the deque.

        Append deque[0] to the output.

    Return the output array.


"""

from collections import deque
import heapq

def subarray_max_two_loops(arr, n, k):
    """
    Brute force
    Time Complexity = O(N * K)
    :param arr:
    :param n:
    :param k:
    :return:
    """
    max = 0
    res = []
    for i in range(n-k+1):
        max = arr[i]
        for j in range(1, k):
            if arr[i+j] > max:
                max = arr[i+j]
        res.append(max)

    return res

def subarray_max_heap(arr, n, k):
    """
    Use Max heap of size k to find the max in each subarray
    Time Complexity - O(N * logk)
    :param arr:
    :param n:
    :param k:
    :return:
    """
    heap = []
    res = []

    for i in range(k):
        heapq.heappush(heap, -1*arr[i])

    res.append(-1*heap[0])

    for i in range(k, n):
        heapq.heappush(heap, -1*arr[i])
        res.append(-1*heap[0])

    return res

def subarray_max_deque(arr, n, k):
    """
    Create a double ended queue that will store indexes of array elements
    The queue will store indexes of useful elements in every window and it will
    maintain decreasing order of values for front(left) to rear(right)

    Time Complexity: O(N)
    """
    qi = deque()
    result = []

    for i in range(k):
        # Maintain decreasing order of elements
        # If incoming element is greater than right element in queueu then pop the right element until queue is empty or right
        # element in queue is greater than current element
        while qi and arr[i] >= arr[qi[-1]]:
            qi.pop()
            print("Inside first k elements, maintain qi in decreasing order")
            print(qi)

        # Add new element at rear of the queue
        qi.append(i)
        print("Inside first k elements, appending index")
        print(qi)

    # Process rest fo the elements, from arr[k] to arr[n-k]
    for i in range(k,n):
        # The element at the front of the queuu is the largest element
        # of previous window, so add to result array
        result.append(arr[qi[0]])

        # Remove elements which are out of the window, the minimum index in a window is i-k
        while qi and qi[0] <= i-k:
            qi.popleft()
            print("Inside rest of elements, remove elements which are out of window")
            print(qi)

        # Remove all elements smaller than the currently being added element
        while qi and arr[i] >= arr[qi[-1]]:
            qi.pop()
            print("Inside rest of elements, maintain qi in decreasing order")
            print(qi)

        qi.append(i)
        print("Inside rest of elements, appending index")
        print(qi)


    print("Outside the for loops")
    print(qi)
    result.append(arr[qi[0]])
    return result

def subarray_max_deque_leetcode(arr, n, k):
    """
    **** Very easy to follow ****
    https://leetcode.com/problems/sliding-window-maximum/solution/
    https://leetcode.com/articles/sliding-window-maximum/#

    Time Complexity = O(N)
    :param arr:
    :param k:
    :return:
    """
    # If either n or k is 0 then return empty list
    if n * k == 0:
        return []

    # If window size in 1 then return the array as it is
    if k == 1:
        return arr

    output = []
    queue = deque()

    def clean_queue(i):
        # If the index at 0 th position is out of this sliding window then pop that element
        if queue and queue[0] == i-k:
            queue.popleft()

        # Always maintain a decreasing order in queue. If current element is greater than queue's last element
        # then pop the queue element
        while queue and arr[queue[-1]] < arr[i]:
            queue.pop()

    for i in range(k):
        # Do  the clean up first
        clean_queue(i)
        queue.append(i)

    # Update output with max element of first k elements
    output.append(arr[queue[0]])

    for i in range(k, n):

        # Do the clean up of queue firt and then add the element
        clean_queue(i)
        queue.append(i)
        output.append(arr[queue[0]])

    return output


def main():
    #arr = [1,2,3,4,5,6,7,8,9,10]
    arr = [1,3,-1,-3,5,3,6,7]
    n = len(arr)
    k = 3
    print("Subarrays max using loop")
    print(subarray_max_two_loops(arr, n, k))

    print("Subarrays max using heap")
    print(subarray_max_heap(arr, n, k))

    print("Subarrays max using Deque")
    print(subarray_max_deque(arr, n, k))

    print("Subarrays max using Deque Leetcode way")
    print(subarray_max_deque_leetcode(arr,n, k))

if __name__ == '__main__':
    main()
