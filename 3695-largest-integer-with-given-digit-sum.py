class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1
        
        digits = [0] * n
        remaining = s
        
        for i in range(n):  # fill from leftmost
            d = min(9, remaining)
            digits[i] = d
            remaining -= d
        
        return int(''.join(map(str, digits)))
