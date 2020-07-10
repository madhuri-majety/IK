"""
A permutation, also called an 'arrangement number' or 'order' is a rearrangement of the elements of an ordered
list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

In recursion, backtrack means that the control reached to dead end, so move back and choose another path.

"""
def permute_util(arr, l, r):
    if (l==r):
        print(arr)
    else:
        for i in range(l, r+1):
            arr[i], arr[l] = arr[l], arr[i]
            permute_util(arr, l+1, r)
            # Revert back the array to original array
            arr[i], arr[l] = arr[l], arr[i]

def permute(arr):
    permute_util(arr, 0, len(arr)-1)


def main():
    l1 = ['1','2','3', '4']
    print("Printing permutations of {}\n".format(l1))
    permute(l1)

if __name__ == '__main__':
    main()
