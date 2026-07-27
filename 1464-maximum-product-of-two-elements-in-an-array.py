class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = float('-inf')
        for x in nums:
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
        return (first - 1) * (second - 1)
