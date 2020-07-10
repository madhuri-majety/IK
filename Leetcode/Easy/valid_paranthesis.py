"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

https://leetcode.com/problems/valid-parentheses/

Algorithm

    Initialize a stack S.

    Process each bracket of the expression one at a time.

    If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later,
    let us simply move onto the sub-expression ahead.

    If we encounter a closing bracket, then we check the element on top of the stack.

    If the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack
    and continue processing. Else, this implies an invalid expression.

    In the end, if we are left with a stack still having elements, then this implies an invalid expression.
"""

def valid_paranthesis(str):
    stack = []

    mapping = {')': '(', '}': "{", "]": "["}

    for char in str:
        if char in mapping:
            if stack:
                top = stack.pop()
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)

        else:
            stack.append(char)

    return not stack

def main():
    print(valid_paranthesis("{}"))
    print(valid_paranthesis("()[]{}"))
    print(valid_paranthesis("(]"))
    print(valid_paranthesis("([)]"))
    print(valid_paranthesis("{[]}"))

if __name__ == '__main__':
    main()
