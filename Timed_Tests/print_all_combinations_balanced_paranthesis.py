"""
Write a function to generate all possible n pairs of balanced parentheses.

Examples:

Input : n=1
Output: {}

Input : n=2
Output:
{}{}
{{}}

https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/

Algorithm:
Keep track of counts of open and close brackets.

Initialize these counts as 0.
Recursively call the _printParenthesis() function until open bracket count is less than the given n.
    If open bracket count becomes more than the close bracket count, then put a closing bracket
        and recursively call for the remaining brackets.
    If open bracket count is less than n, then put an opening bracket and
        call _printParenthesis() for the remaining brackets.

https://leetcode.com/problems/generate-parentheses/solution/

Complexity Analysis (Open above link)

Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n).
This analysis is outside the scope of this article,
but it turns out this is the n-th Catalan number which is bounded asymptotically

​4n​.

    Time Complexity : O(4^n / sqrt(n))  Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity : O(4^n / sqrt(n)) as described above, and using O(n) space to store the sequence.

"""

def generate_paranthesis_util(str, N, open, close, ans):
    if close == N:
        ans.append(str)
        return
    else:
        if open < N:
            generate_paranthesis_util(str+'{', N, open+1, close, ans)

        if close < open:
            generate_paranthesis_util(str+'}', N, open, close+1, ans)

    return ans

def generate_paranthesis(N):
    open = 0
    close = 0
    ans = []
    return generate_paranthesis_util("", N, open, close, ans)

def main():
    print(generate_paranthesis(2))
    print(generate_paranthesis(3))
    print(generate_paranthesis(4))

if __name__ == '__main__':
    main()
