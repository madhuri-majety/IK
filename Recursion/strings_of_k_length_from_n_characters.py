"""
print all possible strings of length k that can be formed from a list of n characters

Problem Solving using : Tail Recursion (Alternatively can be done iteratively as well)

Main Recursion idea:
Consider a prefix which is empty initially and add each element into prefix and again recursively create new strings by
appending element to new string until the length(k) of new string is reached

For a given set of size n, there will be n^k possible strings of length k.
The idea is to start from an empty output string (we call it prefix in following code).
One by one add all characters to prefix. For every character added, print all possible strings with current prefix
by recursively calling for k equals to k-1.


Recursion tree:
- At root level, we have n choices to compute initial prefix which is breadth of the tree
- The depth of the tree depends on k as it represents the number of decisions to be made.
"""

def print_k_length_substrings_util(arr, prefix, size, k):
    if k == 0:
        print(prefix)
        return

    for i in range(size):
        new_prefix = prefix + arr[i]

        # k is decreased as character is added
        print_k_length_substrings_util(arr, new_prefix, size, k-1)

def print_k_length_substrings(arr,k):
    print_k_length_substrings_util(arr, "", len(arr), k)

def main():
    arr = ['a', 'b', 'c', 'd']
    print_k_length_substrings(arr, 2)

if __name__ == "__main__":
    main()
