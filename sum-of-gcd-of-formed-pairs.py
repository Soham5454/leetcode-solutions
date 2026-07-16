from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        running_max = 0
        
        for i in range(n):
            running_max = max(running_max, nums[i])
            prefix_gcd.append(gcd(nums[i], running_max))
        
        prefix_gcd.sort()
        
        left, right = 0, n - 1
        total = 0
        
        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return total
