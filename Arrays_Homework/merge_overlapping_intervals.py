"""
Given an array of time intervals in any order inputArray of size n, merge all overlapping intervals into one
and output the resulting array, such that no two intervals in result array are overlapping.
In other words, result arry should contain only mutually exclusive intervals,

For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }.
The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
Similarly {5, 7} and {6, 8} should be merged and become {5, 8}

Brute force: Iterate over intervals, if the currents start interval is < previous end interval, then they are
              overlapping. If overlapping remove the later interval and merge that to previous interval
              TC - O(N^2)

Efficient approach:
    - Sort the intervals based on the start time
    - push the first interval to the stack
    - For each interval do the following
        - If the current interval does not overlap with the stack top, push current interval to stack
        - If the current interval overlaps with the stack top and ending time of current interval is more
          than that of the stack top, update stack top with the ending time of current interval
    - At the end stack contains the merge intervals
"""

def get_merge_intervals(arr):
    # Sort the list based on the start time (Default the sort function sorts on first element.
    # Don't need to write lambda function here. Just for an example.
    arr.sort(key= lambda x: x[0])

    result = [arr[0]]

    for cur_interval in arr[1:]:
        if result[len(result)-1][1] >= cur_interval[0]:
            result[len(result)-1][1] = max(cur_interval[1], result[len(result)-1][1])
        else:
            result.append(cur_interval)

    return result

def get_merge_intervals_new(arr):
    # Sort the list based on the start time (Default the sort function sorts on first element.
    # Don't need to write lambda function here. Just for an example.
    if len(arr) == 0:
        return []

    arr.sort(key= lambda x: x[0])

    result = [arr[0]]

    for cur_interval in arr[1:]:
        if result[-1][1] >= cur_interval[0]:
            result[-1][1] = max(cur_interval[1], result[-1][1])
        else:
            result.append(cur_interval)

    return result

def main():
    arr = [[1,3], [5,7], [2,4], [6,8]]

    print(get_merge_intervals_new(arr))

if __name__ == '__main__':
    main()


