"""
Print out all the subsets of a set
Set of size N has 2^N subsets

Input: Set as an array.
Output: Subsets in any order
"""


def subsets_util_excl_incl(inp, idx, opt, opt_idx):
    if idx == len(inp):
        print(opt[:opt_idx])
    else:
        # Exclusion - Dont add the chosen element into the output array. Prints null set first
        subsets_util_excl_incl(inp, idx+1, opt, opt_idx)

        # Inclusion - Add the chosen element into the output array
        opt[opt_idx] = inp[idx]
        subsets_util_excl_incl(inp, idx+1, opt, opt_idx+1)

def subsets_excl_incl(arr):
    """
    In this method, we will do exclusion first and start including at the dead end
    :param arr:
    :return:
    """
    n = len(arr)
    op = [None]*n
    subsets_util_excl_incl(arr,0,op,0)

def subsest_util_incl_excl(arr, idx, out):
    # Base case:
    if idx == len(arr):
        print(out)
    else:
        # Do the Inclusion of the chose element from arr
        out.append(arr[idx])
        subsest_util_incl_excl(arr, idx+1, out)

        # Pop the element and then exclude the element of choice
        out.pop()
        subsest_util_incl_excl(arr, idx+1, out)

def subsets_incl_excl(arr):
    """
    In this method we will include first and then exclude the choice we made.
    :param arr:
    :return:
    """
    n = len(arr)
    out = []
    subsest_util_incl_excl(arr, 0, out)


def main():
    arr = [1,2,3]
    print("Printing subsets using exclude and then include mechanism")
    subsets_excl_incl(arr)
    arr1 = ['a','b','c']
    print("Printing subsets using include and then exclude mechanism")
    subsets_incl_excl(arr1)

if __name__ == '__main__':
    main()
