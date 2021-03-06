"""
Implement String To Integer Function


Problem Statement:

Given a string s, which may contain numerical as well as non numerical characters.
You have to extract first integer out of it.

Rules are:

Left most contiguous digits will form the integer, everything after that should be ignored.
("ik45 2" -> 45, because 45 and 2 are not contiguous.)
Sign ('+' or '-') will be effective only if it is just before the integer.
If no sign just before the integer then '+' is applied by default. ("42" -> 42, because '+' is applied by default.
"ik-42" -> -42, because - appears just before 42. "ik- 42" -> 42 because there is a space before 42.)
If there is no number present then return 0. ("Cpp" -> 0.)

Sample Test Cases:

Sample Input 0:

"  ik  +-4 289 ik"

Sample Output 0:

 -4

Sample Input 1:

"- +  -  5ik  "

Sample Output 1:

5

Sample Input 2:

"i-k42ki59"

Sample Output 2:

42

Input Format:

There is only one argument denoting string s.

Output Format:

Return first integer extracted from given string.

Constraints:

0 <= |s| <= 10^5
s may contain numerical as well as non numerical characters.
If number is present then it is guaranteed that it will fit in integer. (No need to think about integer overflow.)
Solution with linear time complexity and constant space is expected.

Notes:

This problem has many variants. Small change in any condition will change the solution.
So clarify any doubts before presenting your solution in interviews.
"""

def string_to_first_integer(word):
    i = 0

    while i < len(word) and not word[i].isdigit():
        i += 1

    sign = 1
    if i != 0 and word[i-1] == '-':
        sign = -1

    ans = 0
    while i < len(word) and word[i].isdigit():
        ans = ans*10 + int(word[i])
        i += 1

    return ans * sign


print(string_to_first_integer("i-k42ki59"))
print(string_to_first_integer("  ik  +-4 289 ik"))
print(string_to_first_integer("-4"))
print(string_to_first_integer("42"))
print(string_to_first_integer("  -42"))

