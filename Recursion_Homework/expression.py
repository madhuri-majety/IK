"""
Given a string of integers as input, put between each pair of digits, of of {"","*","+"} such that the
expression you get will evaluate to k.
Putting an empty string ("") between two numbers mean, that the numbers are joined to form a new number
eg 1 "" 2 = 12

order of integers given as input neeeds to remain the same

input :
string of positve integers
Target K

Output:

All possible strings that evaluate to K

Example:
    If the input is "222" and K = 24
    possible answers are
    22 + 2  2 "" 2 "+" 2
    2+22

Remember the precendence matters
1. join ""
2. Multiplication (*)
3. Addition(+)

"""

"""
Top 3 points :
Lets use sofar, remaining logic
# don't create intermediate variable in recursion. It is hard to keep track of them
# try to induce the rule for 1, 2, 3,...k ... n-1 and n

"""
def add_operators(rest, sofar, cur_value, last_value, res, target):
    """
    This function applies the operators to sofar as operand1 and rest as operand2
    """
    # if rest is None, that means the end of the string is reached.
    # Compare the current value with target and add to result if matches
    print("Inside add_operators()")
    if not rest:
        if cur_value == target:
            res.append(sofar+"="+str(target))
        return
    # Else if rest is not None, then recursively go to the end of the string by applying operators
    for i in range(1, len(rest)+1):
        val = rest[:i]
        if i == 1 or (i > 1 and rest[0] != "0"):
            # Add "+" operand and recursively add "+" operand
            print("'+':", rest[i:], sofar + "+" + val, cur_value+int(val), int(val), res, target)
            add_operators(rest[i:], sofar + "+" + val, cur_value+int(val), int(val), res, target)
            # Add "*" operand and recursively add "*" operand
            print("'*':", rest[i:], sofar + "*" + val, cur_value-last_value+last_value*int(val),
                      last_value*int(val), res, target)
            add_operators(rest[i:], sofar + "*" + val, cur_value-last_value+last_value*int(val),
                      last_value*int(val), res, target)


def generate_all_expressions(s, target):
    """
    Uses the sofar & remaining recursion logic
    For example, str = "123"
    for i = 1, take '1' as operand1 and '23' as operand2 which recursively break and apply operators
    for i = 2, take "12" as operand1 and '3' as operand2 which recursively break and apply operators
    for i = 3, take "123" as operand1 and '' as operand2 which will return back as the second operand is None
    :param s:
    :param target:
    :return:
    """
    # Create result list to update valid expressions
    res = []

    # Break the string to sofar and rest and let the function recursively break the rest and apply operators
    for i in range(1, len(s) + 1):
        if i == 1 or (i > 1 and s[0] != "0"):
            print("Inside generate_all_expressions()")
            print(s[i:], s[:i], int(s[:i]), int(s[:i]), res, target)
            add_operators(s[i:], s[:i], int(s[:i]), int(s[:i]), res, target)
    return res


print("Result for expression '222' with value '24'", generate_all_expressions('222',24), end="\n\n\n")

print("Result for expression '123' with value '6'", generate_all_expressions('123',6))