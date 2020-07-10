"""
* Infix to Postfix Expression
    * Solution:
        * Scan from left to right
        * If operand put it on to the postfix expression
        * If operator push it onto the stack
        * Top of the stack should always be the higher precedence operator
        * If the current scanned operator is of equal or lower precedence then pop the operator from the stack and
            append it to the postfix expression
        * If end of the expression then pop all the operators and append it to the postfix expression
        * Another variation of this expression is to have paranthesis in the expression. Rules for that are as follows
            * Push the open paranthesis to the stack.
            * Append operands to the postfix expression
            * If the closing paranthesis comes, then push all the operators until the open paranthesis is encountered.
            * If before the closing paranthesis, if higher precedence operator comes then push to stack and if lower
                precedence comes next to higher precedence, then pop the higher and equal precedence and operators and
                push the current operator
            * After popping all the operators until open paranthesis and appending it to postfix expression,
                pop the open paranthesis as well.

Pseudo code:

InfixToPostfix(expr):
    create_stack s
    postfix_expr = []
    for i <- 0 to len(expr)-1:
        if expr is operand:
            postfix_expr.append(expr[i])
        elif expr[i] is operator:
            while(!s.isempty() and s.top() >= expr[i]) and (!isopenparanthesis(s.top())):
                postfix_expr.append(s.top())
                s.pop()
            s.push(expr[i])
        elif expr[i] == isopenparanthesis(expr[i]):
            s.push(expr[i])
        elif expr[i] == isclosingparanthesis(expr[i]):
            while(!s.isempty() and !isopenparanthesis(s.top())):
                postfix_expr.append(s.top())
                s.pop()
            # pop the open paranthesis
            s.pop()

    while(!s.isempty):
        opr = s.pop()
        postfix_expr.append(opr)

    return "".join(postfix_expr)

"""