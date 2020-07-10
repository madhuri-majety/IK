"""
 Given a list of daily temperatures T, return a list such that, for each day in the input,
 tells you how many days you would have to wait until a warmer temperature. If there is no future day
 for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""

class Solution(object):
    def daily_temperatures(self, temps):
        days_to_wait_list = []
        for i in range(len(temps)):
            count = 0
            for j in range(i+1, len(temps)):
                #print(temps[i], temps[j])
                if temps[j] > temps[i]:
                    count = j - i
                    break
                else:
                    j = j+1
            days_to_wait_list.append(count)
        return days_to_wait_list

    def daily_temperatures_stack(self, T):
        """

        :param temps:
        :return:
        """
        stack = []
        res = [0] * len(T)

        for idx in range(len(T)):
            while stack and T[stack[-1]] < T[idx]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)

        return res




def main():
    forecast = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    days_to_wait = sol.daily_temperatures(forecast)
    print(days_to_wait)
    print("***********************************")
    print(sol.daily_temperatures_stack(forecast))

if __name__ == '__main__':
    main()
