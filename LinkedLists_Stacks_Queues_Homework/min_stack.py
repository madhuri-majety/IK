"""

Implement A Min Stack

https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/


Problem Statement:

You have to build a min stack. Min stack should support push, pop methods (as usual stack) as well as one method that returns the minimum element in the entire stack.

You are given an integer array named operations of size n, containing values >= -1.
operations[i] = -1 means you have to perform a pop operation.
operations[i] = 0 means you need to find the minimum element in the entire stack and add it at the end of array to be returned.
operations[i] >= 1 means you you need to push operations[i] on the stack.

Input Format:

There is only one argument in input, denoting integer array named operations.

Output Format:

Return an integer array containing answer for each operations[i] = -1.

Constraints:

1 <= n <= 100000
-1 <= operations[i] <= 2 * 10^9
If stack is empty, then do nothing for pop operation.
If stack is empty, then consider -1 as the minimum element.

Sample Test Case:

Sample Input:

[10 5 0 -1 0 -1 0]

Sample Output:

[5 10 -1]

Explanation:

Initially stack = [], ans = [].
operations[0] = 10 -> push -> stack = [10], ans = []
operations[1] = 5 -> push -> stack = [10 5], ans = []
operations[2] = 0 -> get minimum element -> stack = [10, 5], ans = [5]
operations[3] = -1 -> pop -> stack = [10], ans = [5]
operations[4] = 0 -> get minimum element ->stack = [10], ans = [5 10]
operations[5] = -1 -> pop -> stack = [], ans = [5, 10]
operations[6] = 0 -> get minimum element -> stack = [], ans = [5 10 -1] (as stack is empty we have to consider -1 as the minimum element.)


"""

class MinStackBruteForce(object):
    """
    In this solution, we maintain two stacks, one to store actual elements
    and other to store the min at the time of insertion
    Time Complexity for all operations are O(1)
    Space Complexity is O(N) for extra stack.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, elem):
        if not self.stack and not self.min_stack:
            self.stack.append(elem)
            self.min_stack.append(elem)
        else:
            min_elem = min(elem, self.min_stack[-1])
            self.stack.append(elem)
            self.min_stack.append(min_elem)

        print("Acutal Stack after pushing {} : {}".format(elem, self.stack))
        print("Min Stack after pushing {} : {}".format(elem, self.min_stack), end='\n\n')

    def pop(self):
        if self.stack is None:
            return
        self.stack.pop()
        self.min_stack.pop()

        print("Acutal Stack after popping: {}".format(self.stack))
        print("Min Stack after popping: {}".format(self.min_stack), end='\n\n')

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None


class MinStackOptimal(object):
    """
    This solution achieves the operation get_min() in O(1) time and at the same time
    no auxillary data structure used to maintian the min elements.
    push(x): If new elem(x) is greater than minelem, then insert the new elem(x) as it is
            If new elem(x) in smaller than minelem, then insert 2*x-minelem into stack and update minelem to x
    pop(): If elem y is popped and if y is less than minelem, then update minelem = 2*minelem - y
            If elem y is greater than minelem, then minelem will still be minelem
    peek(): if top element is less than minelem then return minelem, else return top element.
    """
    def __init__(self):
        self.stack = []
        self.min = 0

    def get_min(self):
        if not self.stack:
            return -1

        return self.min

    def peek(self):
        if not self.stack:
            return
        top = self.stack[-1]
        if top < self.min:
            return self.min
        else:
            return top

    def push(self,x):
        """
        If the element (x) to be pushed in greater than self.min, append to stack
        If the element (x) to be pushed is smaller than self.min, then append 2*x - self.min into stack
        and update self.min
        :return:
        """
        if not self.stack:
            self.stack.append(x)
            self.min = x
            return
        if x >= self.min:
            self.stack.append(x)
        else:
            self.stack.append((2*x) - self.min)
            self.min = x
        print("After pushing element {}: {}, min is {}".format(x, self.stack, self.min), end='\n\n')

    def pop(self):
        """
        If the popped element(y) is greater than self.min then do nothing
        If the popped element(y) is smaller than self.min then update self.min = 2*self.min - y
        :return:
        """
        if not self.stack:
            return

        top = self.stack[-1]
        self.stack.pop()
        if top < self.min:
            self.min = (2*self.min) - top

        print("After popping element {}: {}, min is {}".format(top, self.stack, self.min), end='\n\n')


def min_stack_optimal_helper(operations):
    res = []
    minstack = MinStackOptimal()
    for i, oper in enumerate(operations):
        if oper == -1:
            minstack.pop()
        elif oper == 0:
            minelem = minstack.get_min()
            res.append(minelem)
        elif oper >=1 :
            minstack.push(oper)

    return res

def min_stack_brute_force_helper(operations):
    res = []
    minstack = MinStackBruteForce()
    for i, oper in enumerate(operations):
        if oper == -1:
            minstack.pop()
        elif oper == 0:
            minelem = minstack.get_min()
            if minelem:
                res.append(minelem)
            else:
                res.append(-1)
        elif oper >=1 :
            minstack.push(oper)

    return res

def main():
    """
    minstack = MinStackBruteForce()
    #minstack.push(0)
    minstack.push(5)
    minstack.push(1)
    minstack.push(6)
    minstack.push(0)
    minstack.push(3)

    print(minstack.get_min())
    minstack.pop()
    print(minstack.get_min())
    minstack.pop()
    print(minstack.get_min())

    sample = [10, 5, 0, -1, 0, -1, 0]
    print("********* Using Bruteforce solution ***********************")
    print("List of min values are: {}".format(min_stack_brute_force_helper(sample)))
    print("***********************************************************")
    """
    minstack = MinStackOptimal()
    # minstack.push(0)
    minstack.push(5)
    minstack.push(1)
    minstack.push(6)
    minstack.push(0)
    minstack.push(3)

    print(minstack.get_min())
    minstack.pop()
    print(minstack.get_min())
    minstack.pop()
    print(minstack.get_min())
    print("Printing top elem: {}".format(minstack.peek()))

    sample = [10, 5, 0, -1, 0, -1, 0]
    print("********* Using Optimal solution ***********************")
    print("List of min values are: {}".format(min_stack_optimal_helper(sample)))
    print("***********************************************************")

if __name__ == '__main__':
    main()
