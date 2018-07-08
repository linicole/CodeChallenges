"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    # this returns a list of tuples of all satisfied pairs
    def twoSum(self, nums, target):
        rest_part = [(target-x) for x in nums]
        results = []
        for i in range(len(rest_part)):
            if rest_part[i] in nums:
                if i != nums.index(rest_part[i]):
                    index_pair = (i, nums.index(rest_part[i]))
                    index_tuple = tuple(sorted(index_pair))
                    results.append(index_tuple)
        return list(set(results))

    # the followings will meet the exact request of the test
    def twoSum_v1(self, nums, target):
        rest_part = [(target-x) for x in nums]
        for i in range(len(rest_part)):
            if rest_part[i] in nums:
                if i != nums.index(rest_part[i]):
                    index_pair = [i, nums.index(rest_part[i])]
                    break
        print(index_pair)

    def twoSum_v2(self, nums, target):
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()  # sort the list by the first item in each tuple
        begin, end = 0, len(nums)-1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return([nums_index[begin][1], nums_index[end][1]])
            elif curr < target:
                begin += 1
            else:
                end -= 1



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 4, 5, 11, 15], 9))


