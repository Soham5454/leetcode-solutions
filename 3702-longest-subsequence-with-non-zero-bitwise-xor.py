class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        has_nonzero = any(num != 0 for num in nums)
        
        if not has_nonzero:
            return 0
        elif total_xor != 0:
            return n
        else:
            return n - 1
