"""
Given a number n, you have to find the next smallest palindromic number, larger than it.

Eg:
Input: 5, Output: 6
Input: 10,Output:11

https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

There can be three different types of inputs that need to be handled separately
1) The input number is Palindrome and has all 9s. input = , output = 1001
2) input number is not palindrome  input = 1234, output = 1331
3) input number is palindrome and doesn't have all 9s or same numerics input = 1221, output = 1331

"""

def isall9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count +=1

    if count == len(nums):
        return True
    return False

def next_palindrome_num_for_non9s(nums):
    n = len(nums)
    # Find the mid index
    mid = n//2

    # end of left side is always mid-1
    i = mid - 1

    # start of right depends on whether number of elements are odd or not
    j = mid if n%2 == 0 else mid+1

    # A boolean value to see if the mirror of left is enough or not
    left_smaller = False

    # Initially ignore the same digits in the middle
    while i >= 0 and nums[i] == nums[j]:
        i -= 1
        j += 1

    # Find if the middle digit needs to be incremented or not
    # Two cases to consider -
    #  - if given number is already a palindrome in itself
    #  - if the left element is smaller than right element
    if i < 0 or nums[i] < nums[j]:
        left_smaller = True

    # Copy mirror of left to right
    while i >= 0:
        nums[j] = nums[i]
        i -= 1
        j += 1

    if left_smaller:
        carry = 1

        # If there are odd digits, then increment
        # the middle and store the carry
        if n % 2 == 1:
            nums[mid] += carry
            carry = nums[mid] // 10
            nums[mid] %= 10

        # Reset the values of left (i) and right (j)
        i = mid - 1
        j = mid if n%2 ==0 else mid + 1


        while i >= 0:
            nums[i] = nums[i]+carry
            carry = nums[i]//10
            nums[i] %= 10
            # Copy left side to right side
            nums[j] = nums[i]
            i -= 1
            j += 1

    return nums



def next_palindrome_num(num):
    # Convert the number into list of digits
    nums = [int(x) for x in str(num)]

    new_num = []

    if isall9(nums):
        new_num.append(1)
        for i in range(len(nums)-1):
            new_num.append(0)
        new_num.append(1)
    else:
        new_num = next_palindrome_num_for_non9s(nums)

    new_str = ''.join(str(i) for i in new_num)
    return new_str



def main():
    print(next_palindrome_num("99"))
    print(next_palindrome_num("12921"))
    print(next_palindrome_num("125322"))  # case 2.1
    print(next_palindrome_num("713322"))  # case 2.2

if __name__ == '__main__':
    main()