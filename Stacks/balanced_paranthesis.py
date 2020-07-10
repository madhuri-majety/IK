"""
* Balanced Parenthesis:
    * Crux: Last unclosed, first closed
    * Solution:
        * Scan from left to right
        * If Opening symbol, push it to the stack
        * If Closing symbol and top of stack is opening of same symbol type, then pop
        * Stack should be empty, if not then it is not a balanced parenthesis expression

Pseudo Code:
def is_balanced_paranthesis(expr):
    create_stack s
    for i <- 0 to len(expr):
        if (isopenparanthesis(expr[i]):
            s.push(expr[i])
        elif isclosingparanthesis(expr[i]):
            if (s.isempty() or s.top() does not pair with expr[i]):
                return False
            else:
                s.pop()
    return(s.isempty())
"""