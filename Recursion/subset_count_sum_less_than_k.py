"""
Given an array, return the count of subsets whose sum of values is less than k

Top Points:
- Exclude all the elements first and start including and check for the sum, if the sum is less than k start including
more elements
- Base condition: If reached to the last element in the array, check if sum < k and return the value if true, which gets
                    accumulated to count
- Recursive idea: The choice to make here is based on the sum < k, if yes, recurse to include more elements
"""

def _helper(a, idx, total, k):
    if idx == len(a):
        return int(total < k)
    else:
        # Exclude first and reach depth of the execution tree
        count = _helper(a, idx+1, total, k)
        #print("Count after exclude:", count)
        # Now start including the element at the level of tree and recursivley add to see if sum is less than k.
        if total + a[idx] < k:
            count += _helper(a, idx+1, total+a[idx], k)
            #print("Count after include:", count)
    return count

def subset_count(arr,k):
    return _helper(arr, 0, 0, k)

def main():
    l1 = [1,2,3]
    k = 4
    print("Printing the count of subsets whose sum is less than {}:  {}".format(k, subset_count(l1,k)))

if __name__ == '__main__':
    main()
