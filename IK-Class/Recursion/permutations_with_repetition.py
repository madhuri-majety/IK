"""
Given a string of length n, print all permutation of the given string.
Repetition of characters is allowed. Print these permutations in lexicographically sorted order

No of permutations for repetition is n^n
Eg for input AB, pemutations with repetition are 4 as below
AA
AB
BA
BB

Problem solving using Recursion
Recursion idea: Iterate over the list of characters in a string and for every choice iterate over again through the  original
list of characters and start appending to the output string until the output string is same as the length of the input
string

"""

def permutations_repetition_util(arr, n, op, op_idx):
    # Base Condition
    if op_idx == n:
        print("".join(op))
        return

    # Recursive transitions
    for i in range(n):
        op.append(arr[i])
        permutations_repetition_util(arr, n, op, op_idx+1)
        # Backtrack
        op.pop()

def permutations_repetition_count(str):
    arr = []
    for i in str:
        arr.append(i)
    permutations_repetition_count_util(arr, len(arr), [], 0)


def permutations_repetition(str):
    arr = []
    for i in str:
        arr.append(i)
    permutations_repetition_util(arr, len(arr), [], 0)

def main():
    str = "ABC"
    print("Printing permutations with repetition for string {} \n:{}".format(str, permutations_repetition(str)))
    #print("Printing count of permutations with repetition {} \n: {}".format(str, permutations_repetition_count(str)))

if __name__ == '__main__':
    main()