"""

Largest Rectangular Area in a Histogram | Set 2

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number
of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
 The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)

https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

Algorithm:
1) Create an empty stack.

2) Start from first bar, and do following for every bar hist[i] where i varies from 0 to n-1.
a) If stack is empty or hist[i] is higher than the bar at top of stack, then push index the i to stack.
b) If this bar is smaller than the top of stack, then keep removing the top of stack while top
of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar.
For hist[tp], the left index is previous (previous to tp) item in stack and right index is i (current index).

3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.


"""

def top(s):
    if len(s) > 0:
        return s[len(s)-1]


def find_max_area_brute_force(hist):
    """
    At every bar in histogram, expand towards left and right until the current bar is less than or equal to left or right.
    Breaking point is when a bar less than current bar is encountered we need to stop expanding and calculate the area with
    height as value of current bar and width as distance between left and right pointers.
    Calculate the area for every bar and update the max area when required.
    Time Complexity : O(N^2)
    Space Complexity: O(1)
    :param hist:
    :return:
    """
    max_area = -1
    size = len(hist)
    for i in range(size):
        cur_height = hist[i]
        print("i: {}, curr_height: {}".format(i, cur_height))
        left = i-1
        right = i+1

        # Now expand to the left until the height of current bar is less than or equal
        # to the bar we are comparing
        while left >= 0 and cur_height < hist[left]:
            left -= 1

        print("i : {}, left : {}".format(i, left))

        # Now expand to the right until the height of current bar is less than or equal to the bar
        # we are comparing with while traversing
        while right < size and cur_height <= hist[right]:
            right += 1
        print("i : {}, right : {}".format(i, right))

        area = (right-left-1) * cur_height
        print("i : {}, area: {}".format(i, area))

        if area > max_area:
            max_area = area

    print("Inside before returning : {}".format(max_area))
    return max_area

def find_max_area(hist):
    stack = []
    max_area = 0
    tp, i = 0, 0
    n = len(hist)

    while i < n:
        print("\n")
        #print("Current Index:{}".format(i))
        # If stack is empty or incoming bar is higher than the
        # the top of the stack, push the current index to stack
        if not stack or hist[i] >= hist[top(stack)]:
            stack.append(i)
            print("Stack is empty or incoming bar is higher than top of stack. So pushed {} to stack".format(i))
            i += 1
            print("Stack after pushing: {}".format(stack))

        # If incoming bar is lower than the top of the stack, then
        # calculate area of rectangle with stack top as the smallest bar
        # i is the right index for the top element before top in stack is left index
        else:
            tp = stack.pop()
            print("Incoming bar {} lower, so popped the stack top, top index : {}".format(i,tp))
            print("Stack after popping:{}".format(stack))

            # Calculate the area with hist[tp] stack as smallest bar
            if len(stack) == 0:
                area_with_top = hist[tp] * i
            else:
                area_with_top = hist[tp] * (i-top(stack)-1)

            # update max_area
            if max_area < area_with_top:
                max_area = area_with_top
            print("Area with top: {}".format(area_with_top))
            print("Max Area: {}".format(max_area))
            print("Current index: {}".format(i))

    while stack:
        tp = stack.pop()
        print("Popping after traversing whole list. Stack is {}".format(stack))
        area_with_top = hist[tp] * (i if len(stack) == 0 else i-tp-1)
        print("i :{}, tp: {}, area_with_top:{}".format(i,tp,area_with_top))


        if max_area < area_with_top:
            max_area = area_with_top
    return max_area

def main():
    print("***** Printing area using Stack *****")
    #print(find_max_area([6, 2, 5, 4, 5, 1, 6]))
    print(find_max_area([1,8,6,2,5,4,8,3,7]))
    #print(find_max_area([1,2,3,4,5,6]))

    #print(find_max_area([5,2,4,6,5,8,1]))


    #print(find_max_area([2, 1, 2, 3, 1]))
    print("\n\n")

    print("*****Priting Area using Brute force method*****")
    #print(find_max_area_brute_force([6, 2, 5, 4, 5, 1, 6]))
    print(find_max_area_brute_force([1,8,6,2,5,4,8,3,7]))

if __name__ == "__main__":
    main()
