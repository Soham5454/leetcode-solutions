# 1. Two Sum
# Difficulty: Easy
# Approach: Hashmap
# Runtime: 0ms - Beats 100%

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
