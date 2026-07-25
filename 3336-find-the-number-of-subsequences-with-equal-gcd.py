from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = defaultdict(int)
        dp[(0, 0)] = 1  
        for num in nums:
            new_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD

                ng1 = gcd(g1, num) if g1 else num
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD

                ng2 = gcd(g2, num) if g2 else num
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD

            dp = new_dp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + cnt) % MOD
        return ans
