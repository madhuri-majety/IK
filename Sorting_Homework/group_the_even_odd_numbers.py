"""
Group the even numbers to the left of the array and odd numbers to the right of the array.

Key Idea: Like quick sort partition, use the even odd criteria as a pivot and move all even numbers to the left
and odd numbers towards the right

Time Complexity: O(N) : Single for loop
Space Complexity: O(1) as it is in-place algorithm
Stable: Yes

"""

def group_odd_even(arr):
    pindex = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            arr[pindex], arr[i] = arr[i], arr[pindex]
            pindex += 1



def main():
    list = [4,1,2,3,4]
    print("Printing list before grouping the elements:", list)
    group_odd_even(list)
    print("Printing list after grouping the elements:", list)

    list1 = [2,2,2,6,6,3,3,8,8,8,8,9,1]
    print("Printing list1 before grouping the elements:", list1)
    group_odd_even(list1)
    print("Printing list1 after grouping the elements:", list1)

    list2 = [1,1,1,1,1]
    print("Printing list1 before grouping the elements:", list2)
    group_odd_even(list2)
    print("Printing list1 after grouping the elements:", list2)

    list3 = []
    print("Printing list1 before grouping the elements:", list3)
    group_odd_even(list3)
    print("Printing list1 after grouping the elements:", list3)


if __name__ == '__main__':
    main()