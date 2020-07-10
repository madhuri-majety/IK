"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
import sys
def best_time_to_sell_stock(arr):
    """
    Single pass solution
    Time Complexity = O(N)
    :param arr:
    :return:
    """
    n = len(arr)
    minprice = sys.maxsize
    max_profit = 0

    # Use the Greedy approach mechanism by updating the minprice at every iteration
    for i in range(n):
        if arr[i] < minprice:
            minprice = arr[i]
        elif arr[i] - minprice > max_profit:
            max_profit = arr[i] - minprice

    print(max_profit)

def main():
    inp1 = [7,1,5,3,6,4]
    inp2 = [7,6,4,3,1]

    best_time_to_sell_stock(inp1)
    best_time_to_sell_stock(inp2)


if __name__ == '__main__':
    main()
