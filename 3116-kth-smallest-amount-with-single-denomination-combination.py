from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def count(x):
            total = 0
            for size in range(1, n + 1):
                for combo in combinations(coins, size):
                    l = 1
                    for c in combo:
                        l = lcm(l, c)
                        if l > x:
                            break
                    if l <= x:
                        term = x // l
                        if size % 2 == 1:
                            total += term
                        else:
                            total -= term
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        
        return lo
