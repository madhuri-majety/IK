"""
* Postfix Expression Evaluation
    * Solution:
        * Scan from left to right
        * If the element is operand, push it to the stack
        * If the element is operator, pop the top elements in stack twice. First popped is second operand and second popped is first operand (This order of operand matters for addition or subtraction)
        * Perform operation on popped two operands and the operators from postfix expression
        * Push the result of the operation back to stack
        * Continue until the last element in postfix expression
        * Final result is stored on the top of the stack and its the only element in the stack
        * Return the result
* Prefix Expression Evaluation:
    * Solution:
        * Scan the prefix expression from right to left
        * If the element is operand, push it to the stack
        * If the element is operator, pop the top elements in the stack twice. First popped is first operand, second popped is second operand (This order of operand matters)
        * Perform operation on popped two operands and the current operator
        * Push the result to the stack
        * Continue until the last element of the the expression
        * Final result is stored on the top of the stack and return the result

Psuedo Code:
EvaluatePostfix(expr):
    create_stack s
    for i <- 0 to len(expr):   <------------
        if expr[i] is operand:
            s.push(expr[i])
        elif expr[i] is operator:
            op2 = s.pop()
            op1 = s.pop()
            result = perform_operation(expr[i], op1, op2)
            s.push(result)
    return s.pop()

EvaluatePrefix(expr):
    create_stack s
    for i <- len(exp) to 0:   <-----------
        if expr[i] is operand:
            s.push(expr[i])
        elif expr[i] is operator:
            op1 = s.pop()
            op2 = s.pop()
            result = perform_operation(expr[i], op1, op2)
            s.push(result)
    return s.pop()
"""
