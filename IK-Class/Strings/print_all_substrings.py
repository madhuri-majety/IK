"""
Print all the substrings of a string
Input :  abcd
Output : a,ab,abc,abcd, b,bc,bcd,c,cd,d = 4(4+1)//2 = 10 substrings
Number of substrings in a string = n(n+1)/2

First character appears n times, second character appear n-1 times as first character and so on
n+(n-1)+(n-2)+(n-3)+...1 = n(n+1)/2
 to find all substrings it takes O(N^3) in brute force solution because we need to pick
the starting and ending point and print all the characters in between starting and ending point and then slide furthur
and repeat

"""
from __future__ import print_function

def print_all_substrings_brute_force_1(s,n):
    """
    We can run three nested loops
    Outer loop picks the starting character
    Middle loop picks the ending character
    Inner loop prints from currently picked starting point to picked ending point.
    TC = O(N^3) for  3 loops
    SC = O(N) as using array to store intermediate values.
    :param s:
    :return:
    """
    for i in range(n):
        for j in range(i+1, n+1):
            res = []
            for k in range(i, j):
                # Append all the charactes in this loop and club them to string before picking the new end point
                res.append(s[k])
            print("".join(res))

def print_all_substrings_brute_force_2(s,n):
    """
    We can run three nested loops
    Outer loop picks the starting character
    Middle loop picks the ending character
    Inner loop prints from currently picked starting point to picked ending point.
    TC = O(N^3) for  3 loops
    SC = O(1) as no extra space is used

    :param s:
    :return:
    """
    for i in range(n):
        for j in range(i+1, n+1):
            for k in range(i, j):
                # ***** By putting the end as '' we automatically append the character in that loop.
                print(s[k], end='')
            print()


def print_all_substrings_using_slicing(s,n):
    for i in range(n):
        for j in range(i+1, n+1):
            print(s[i:j])

def main():
    input = 'arts'
    n = len(input)
    print("****** Printing using extra space ********")
    print_all_substrings_brute_force_1(input, n)

    print("****** Printing using no extra space ********")
    print_all_substrings_brute_force_2(input, n)

    print("****** Printing using slicing ********")
    print_all_substrings_using_slicing(input, n)


if __name__ == '__main__':
    main()


