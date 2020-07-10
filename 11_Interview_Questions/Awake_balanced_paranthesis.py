"""
Given a string with paranthesis return 0 if balanced or -1 for unbalanced paranthesis

Construct an array with 0 for balanced paranthesis or -1 for unbalanced part all non-paranthesis are 0's
input = ((abc)*d+(ab+ad)))
output = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1]
"""

OPEN_PARAN = '('
CLOSED_PARAN = ')'

def check_balanced_paranthesis(str):
    chars = list(str)
    stack = []
    output = [0] * len(chars)

    for i, item in enumerate(chars):
        if item == OPEN_PARAN:
            stack.append(i)
        elif item == CLOSED_PARAN:
            if stack:
                stack.pop()
            else:
                output[i] = -1
        else:
            continue

    for idx in stack:
        output[idx] = -1

    print(output)

check_balanced_paranthesis('((abc)*d+(ab+ad)))')
check_balanced_paranthesis('(a+b))')
check_balanced_paranthesis('((a+b)')

