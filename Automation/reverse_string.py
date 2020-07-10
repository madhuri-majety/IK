"""
Reverse a string

Implement different ways to implement string reversal
import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 10

timeit.repeat(lambda: reverse_string_slicing(s))
[0.6848115339962533, 0.7366074129968183, 0.7358982900041156]

timeit.repeat(lambda: reverse_string_reversed_iterator(s))
[5.514941683999496, 5.339547180992668, 5.319950777004124]

timeit.repeat(lambda: reverse_string_normal_loop(s))
[48.74324739299482, 48.637329410004895, 49.223478018000606]

Algorithm	            Execution Time	Slowdown
Slicing	                0.72s	        1x
reversed + join	        5.39s	        7.5x
Classic / In-Place	    48.87s	        67.9x

"""

def reverse_string_slicing(s):
    return s[::-1]

def reverse_string_reversed_iterator(s):
    return ("".join(reversed(s)))

def reverse_string_normal_loop(s):
    # Convert string into list of characters
    chars = list(s)

    for i in range(len(s)//2):
        chars[i], chars[len(s)-1-i] = chars[len(s)-i-1], chars[i]

    return ("".join(chars))

class Solution(object):
    def reverseStringUtil(self, chars, start, end):
        if start < end:
            chars[start], chars[end] = chars[end], chars[start]
            self.reverseStringUtil(chars, start+1, end-1)

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        chars = list(s)
        self.reverseStringUtil(chars, 0, len(chars)-1)
        print("".join(chars))


def main():
    s = "Madhuri"
    #print(reverse_string_slicing(s))
    #print(reverse_string_reversed_iterator(s))
    #print(reverse_string_normal_loop(s))

    rs = Solution()
    rs.reverseString("Madhuri")
    """
    print("Printing Performace Metrics")
    timeit.repeat(lambda: reverse_string_slicing(s)))
    timeit.repeat(lambda : reverse_string_reversed_iterator(s))
    timeit.repeat(lambda : reverse_string_normal_loop(s))
    """

if __name__ == '__main__':
    main()
