from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix_sum[i]

            total = suffix_sum[i]
            best_opponent = float('inf')
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                best_opponent = min(best_opponent, dp(i + X, max(M, X)))

            return total - best_opponent

        return dp(0, 1)
