"""

Count substrings that starts with character X and ends with character Y

Given a string str of n lowercase characters, the task is to count the number of substrings of str starting with character X and ending with character Y.

Examples:

Input: str = "abbcaceghcak"
        x = 'a', y = 'c'
Output: 5
abbc, abbcac, ac, abbcaceghc, aceghc

Input: str = "geeksforgeeks"
        x = 'g', y = 'e'
Output: 6

https://www.geeksforgeeks.org/count-substrings-that-starts-with-character-x-and-ends-with-character-y/

Approach:
Initialize two counters tot_count and count_x to 0
Traverse through the string
If current character is X then increament count_x
If current character is Y then it means string ends with Y so increment the total count
    tot_count = tot_count + count_x
It means that if there exists a Y then it will make a substring with all the X occurs before Y in the string.
So add the count of X to total count.
Return total count
"""

def count_substrings(str, x, y):
    tot_count = 0
    count_x = 0

    for i in range(len(str)):
        if str[i] == x:
            count_x += 1
        if str[i] == y:
            tot_count += count_x

    print(tot_count)

def print_substrings(str, x, y):
    tot_count = 0
    count_x = 0
    pos_x = []
    result = []

    for i in range(len(str)):
        if str[i] == x:
            count_x += 1
            pos_x.append(i)
        if str[i] == y:
            tot_count += count_x
            for pos in pos_x:
                result.append(str[pos:i+1])

    print(result, tot_count)

def main():
    count_substrings("abbcaceghcak", 'a', 'c')
    count_substrings("geeksforgeeks", 'g', 'e')
    count_substrings("aaaaa", 'a', 'b')

    print("\nPrinitnng Substrings")
    print_substrings("abbcaceghcak", 'a', 'c')
    print_substrings("geeksforgeeks", 'g', 'e')
    print_substrings("aaaaa", 'a', 'b')

if __name__ == '__main__':
    main()
