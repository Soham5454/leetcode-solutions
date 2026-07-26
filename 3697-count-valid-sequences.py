MOD = 10**9 + 7

class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        if k > n:
            return 0
        
        max_n = n + 10  # enough room for factorials
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD
        
        def comb(a, b):
            if b < 0 or b > a or a < 0:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD
        
        total = comb(n - 1, k - 1)
        
        all_odd = 0
        if (n - k) >= 0 and (n - k) % 2 == 0:
            m = (n - k) // 2
            all_odd = comb(m + k - 1, k - 1)
        
        return (total - all_odd) % MOD
