"""
Longest Substring With Balanced Parentheses

Find the length of the longest substring that has matching opening and closing paranthesis

Problem Statement:

Given a string named brackets containing only '(' and ')'. You have to find the length of the longest sub-string
that has balanced parentheses. We only need length, not the sub-string itself.

Input Format:

There is only one argument in input, denoting string named brackets.

Output Format:

Return an integer, denoting the length of the longest sub-string that has balanced parentheses.

Constraints:

1 <= |brackets| <= 10^5
Input string only contains '(' and ')' characters.

Sample Test cases:

Sample Input 1:

"((((())(((()"

Sample Output 1:

4

Explanation 1:

"(())"

Sample Input 2:

"()()()"

Sample Output:2:

6

Explanation 2:

"()()()"


Key Points:
- If starting paran, push the INDEX to the stack
- When closing paran, pop the element from the stack and get the top of the stack if elements in stack or -1
to calculate the distance for that balanced paranthesis
"""

STARTING_PARAN = '('

def find_max_length_of_matching_paranthesis(brackets):
    if len(brackets) == 0:
        return 0
    stack = []
    prev_start, max_len, start = 0, 0, 0

    for i, bracket in enumerate(brackets):
        if bracket == STARTING_PARAN:
            stack.append(i)

        else:
            stack.pop()
            if not stack:
                start = -1
            else:
                start = stack[-1]

            size = i - start
            max_len = max(size, max_len)

    return max_len

def main():
    inp = "()()()"
    #inp = "((((("
    print(find_max_length_of_matching_paranthesis(inp))

if __name__ == '__main__':
    main()
