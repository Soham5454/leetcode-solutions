class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return gcd(smallest, largest)
