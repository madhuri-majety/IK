"""
Given an array of integers, return indices of the two numbers such that thye add up to specific target

Given nums = [2,7,11,15], target = 9
return (0,1)
"""

class TwoSum(object):
    def two_loops_first_occurance(self, nums, target):
        for i in range(len(nums)):
            val1 = nums[i]
            val2 = target - val1
            for j in range(i, len(nums)):
                if nums[j] == val2:
                    return(i,j)

    def two_loops_all_occurances(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] == target-nums[i]:
                    result.append((i,j))

        return result

    def hash_map(self, nums, target):
        hash = {}
        result = []
        for ind, key in enumerate(nums):
            hash[key] = ind

        #print(hash)
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hash:
                #result.append((i,hash[second]))
                return [i, hash[second]]

        return result

    def hash_map_leet_code(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [i, num_to_index[target-num]]

            num_to_index[num] = i

        return []



def main():
    twosum = TwoSum()
    print(twosum.two_loops_first_occurance([2,6,11,7,1,8], 9))
    print(twosum.two_loops_all_occurances([2,6,11,7,1,8], 9))
    print(twosum.hash_map([2,6,11,7,1,8], 9))
    print(twosum.hash_map_leet_code([2,6,11,7,1,8], 9))


if __name__ == '__main__':
    main()


