"""
Find four elements that sum to a given value

"""

class Solution(object):
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        self.size = len(arr)

    def find_four_elements_brute_force(self):
        """
        In  this brute force, generate all possible quadruples and compare the sum
        TC - O(N^4)
        :return:
        """
        result = []
        for i in range(self.size-3):
            for j in range(i+1, self.size-2):
                for k in range(j+1, self.size-1):
                    for l in range(k+1, self.size):
                        if self.arr[i] + self.arr[j] + self.arr[k] + self.arr[l] == self.target:
                            result. append([self.arr[i], self.arr[j], self.arr[k], self.arr[l]])

        print("find_four_elements_brute_force() : {}".format(result))

    def find_four_elements_two_pointers(self):
        """
        In this method like 3 sum problem will use two pointers one from starting and one from ending
        to find the last elements. As it is four sum the first two elements has to be fixed and last two
        elements can be found from two pointers. To do this we need to sort the list.
        TC = O(N^3)

        :return:
        """
        result = []
        A = sorted(self.arr)
        for i in range(self.size-3):
            for j in range(i+1, self.size-2):
                l = j+1
                r = self.size - 1

                while l < r:
                    sum = A[i] + A[j] + A[l] + A[r]
                    if sum == self.target:
                        result.append([A[i], A[j], A[l], A[r]])
                        l = l + 1
                        r = r - 1
                    elif sum > self.target:
                        r = r - 1
                    else:
                        l = l + 1

        print("find_four_elements_two_pointers() : {}".format(result))

    def find_four_elements_hashmap(self):
        """
        1. Store sum of all pairs in hash table with sum as keys and value as tuple of indices.
           Can override the value if the same sum is found so to avoid duplicates
        2. Traverse through array again now fixing first and second elements and Target - (Sum of current pairs) in
        hash table.
        3. If a pair is found then find that all indices are unique
        Time Complexity = O(N^2 + N^2)
        Space Complexity = O(N)
        :return:
        """
        sums_map = {}
        result = []
        #print("\n*****************************\n")
        #print(self.arr)
        for i in range(self.size-1):
            for j in range(i+1, self.size):
                sums_map[self.arr[i] + self.arr[j]] = {i,j}

        #print("Debug: Printing Sums map -- {}".format(sums_map))

        for i in range(self.size-1):
            for j in range(i+1, self.size):
                cur_sum = self.arr[i] + self.arr[j]

                #print("current sum is ", cur_sum)
                #print("Target is {}".format(self.target))
                #print("target - current sum", self.target - cur_sum)
                remaining = self.target - cur_sum
                if remaining in sums_map.keys():
                    #print("Hashtables set & current set is :{}, {}, {}".format(sums_map[remaining], i, j))
                    if sums_map[remaining].isdisjoint({i,j}):
                        #print("Disjoint sets")
                        result.append([self.arr[list(sums_map[remaining])[0]],
                                      self.arr[list(sums_map[remaining])[1]],
                                      self.arr[i],
                                      self.arr[j]])

        print("find_four_elements_hashmap() : {}".format(result))



def main():
    arr = [10,2,3,4,5,9,7,8]
    target = 23
    sol = Solution(arr, target)
    sol.find_four_elements_brute_force()
    sol.find_four_elements_two_pointers()
    sol.find_four_elements_hashmap()

if __name__ == '__main__':
    main()
