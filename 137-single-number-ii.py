class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for bit in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> bit) & 1
            
            if bit_sum % 3 != 0:
                result |= (1 << bit)
        
        if result >= 2**31:
            result -= 2**32
        
        return result
