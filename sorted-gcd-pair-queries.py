from bisect import bisect_right
from math import comb
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        cnt = [0] * (max_val + 1)
        for x in nums:
            cnt[x] += 1
        
        multiples = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            total = 0
            for m in range(d, max_val + 1, d):
                total += cnt[m]
            multiples[d] = total
        
        exact = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total = comb(multiples[d], 2)
            for m in range(2 * d, max_val + 1, d):
                total -= exact[m]
            exact[d] = total
        
        cum = [0] * (max_val + 1)
        running = 0
        for d in range(1, max_val + 1):
            running += exact[d]
            cum[d] = running
        
        answer = []
        for q in queries:
            lo, hi = 1, max_val
            while lo < hi:
                mid = (lo + hi) // 2
                if cum[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            answer.append(lo)
        
        return answer
