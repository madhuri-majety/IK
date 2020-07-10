"""
https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/
https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/

This algorithm follows the priciples of Insertion sort.
Pick an element in second array and fit that in a right place in first array.

Algorithm follows like this:
Iterate through the elements in second array from last element. Do the following for every iteration of ar2[i]
    - Store the last element of ar1[
    - Intialize ar1's traverse pointer j to last but one element in ar1 i.e m-2 with m being the size of ar1
      (excluding the stored last element)
    - Compare the last but one element in ar1 to element ar2[i]
    - Traverse ar1 backward until ar1[j] > ar2[i], and shifing elements in ar1 to right to make room for ar2's
      element into ar1
    - If the shifting happened, the copy the ar2's element into new created space in ar1 and copy the last element
      stored to ar2[i]'s position. To check if shifting happened or not simply check if j == m-2 or not, if not then
      the shifting happened.

"""

def merge_two_arrays_no_extra_space(arr1, arr2, m, n):
    """
    Time Complexity = O(M*N)
    Space Complexity = O(1)
    :param arr1:
    :param arr22:
    :param m:
    :param n:
    :return:
    """
    for i in range(n-1, -1, -1):
        last = arr1[m-1]
        j = m-2

        # Make room for arr2's element into arr1
        while j > 0 and arr1[j] > arr2[i]:
            arr1[j+1] = arr1[j]
            j -= 1

        # If a right place is found for arr2's element
        if j != m-2 or last > arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last


def main():
    ar1 = [1, 5, 9, 10, 15, 20]
    ar2 = [2, 3, 8, 13]
    m = len(ar1)
    n = len(ar2)

    merge_two_arrays_no_extra_space(ar1, ar2, m, n)
    print("First Array is : {}".format(ar1))
    print("Second array is : {}".format(ar2))

if __name__ == '__main__':
    main()


