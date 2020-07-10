"""
Write a function that checks if the given input string has matching opening and closing paranthesis
"""

def is_matching_pair(char1, char2):
    if char1 == '[' and char2 == ']':
        return True
    elif char1 == '(' and char2 == ')':
        return True
    elif char1 == '{' and char2 == '}':
        return True
    else:
        return False

def are_paranthesis_balanced(instr):
    if len(instr) == 0:
        return True
    stack = []

    for i, char in enumerate(instr):
        if char is '[' or char is '(' or char is '{':
            stack.append(char)

        if char is ']' or char is ')' or char is '}':
            if not stack:
                return False
            elif not is_matching_pair(stack.pop(), char):
                return False

    if not stack:
        return True
    else:
        return False

def main():
    inp = "{(1+2)}"

    if are_paranthesis_balanced(inp):
        print("Balanced")
    else:
        print("Not Balanced")

if __name__ == '__main__':
    main()
