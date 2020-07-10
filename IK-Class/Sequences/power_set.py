"""
Power Set Power set P(S) of a set S is the set of all subsets of S.
For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

**** If S has n elements in it then P(s) will have 2^n elements *****
https://www.geeksforgeeks.org/power-set/

Input: Set[], set_size
1. Get the size of power set
    powet_set_size = pow(2, set_size)
2  Loop for counter from 0 to pow_set_size
     (a) Loop for i = 0 to set_size
          (i) If ith bit in counter is set
               Print ith element from set for this subset
     (b) Print separator for subsets i.e., newline

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc

Time Complexity - O(n * 2 ^n)

Power Set <===> Subsets
"""
import math

def print_power_set(arr):
    n = len(arr)
    two_power_n = int(math.pow(2, n))

    # Iterate from 0 to 2^n -1
    for counter in range(0, two_power_n):
        # Iterate over given array
        for i in range(n):
            if counter & (1 << i) > 0:
                print(arr[i], end='')
        print("")


def main():
    arr = ['a', 'b', 'c']
    print_power_set(arr)
    print("\n")
    print_power_set([1,2,3])

if __name__ == '__main__':
    main()
