"""
Given an array, print the subsets whose sum of values is less than k

Top Points:
- Exclude all the elements first and start including and check for the sum, if the sum is less than k start including
more elements
- Base condition: If reached to the last element in the array and total < k, print the output subset
- Recursive idea: The choice to make here is based on the sum < k, if yes, recurse to include more elements
"""

def _helper(a, idx, total, op, op_idx, k):
    if idx == len(a) and total < k:
        print(op[:op_idx])
    else:
        # First exclude first and reach the depth until it reaches null
        _helper(a, idx+1, total, op, op_idx, k)

        # Now add element at level in array to total and check if sum < k, if yes then add that to the output array
        if total + a[idx] < k:
            op[op_idx] = a[idx]

            # Now add more elements recursively until sum is less than k
            _helper(a, idx+1, total+a[idx], op, op_idx+1, k)

def subset_count(arr,k):
    op = [None] * len(arr)
    _helper(arr, 0, 0, op, 0, k)

def main():
    l1 = [1,2,3]
    k = 4
    print("Printing the count of subsets whose sum is less than {}:\n".format(k))
    subset_count(l1, k)

if __name__ == '__main__':
    main()
