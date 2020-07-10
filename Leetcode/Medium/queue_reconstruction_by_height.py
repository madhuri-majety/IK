"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers
(h, k), where h is the height of the person and k is the number of people in front of this person who have a
height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Solution:
Algorithm

    Sort people:
        In the descending order by height.
        Among the guys of the same height, in the ascending order by k-values.

    Take guys one by one, and place them in the output array at the indexes equal to their k-values.

    Return output array.

https://leetcode.com/problems/queue-reconstruction-by-height/solution/
"""

class Solution(object):
    def reconstructQueue(self, people):
        # Sort the people list in descending order for heights and
        # ascending value of k
        people.sort(key = lambda x: (-x[0], x[1]))
        print("Debug: Printing sorted list - {}".format(people))

        # Take an output array and iterate through the sorted list
        # and insert the values in output array based on their k-value
        output = []
        for p in people:
            output.insert(p[1], p)

        print("Debug: Before Returning the reconstructed queue is {}".format(output))
        return output


def main():
    sol = Solution()
    input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(sol.reconstructQueue(input))

if __name__ == '__main__':
    main()



