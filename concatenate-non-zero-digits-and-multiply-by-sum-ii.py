class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        
        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)
        prefix_x = [0] * (n + 1)
        
        for i in range(n):
            d = int(s[i])
            prefix_sum[i+1] = prefix_sum[i] + d
            if d != 0:
                prefix_count[i+1] = prefix_count[i] + 1
                prefix_x[i+1] = (prefix_x[i] * 10 + d) % MOD
            else:
                prefix_count[i+1] = prefix_count[i]
                prefix_x[i+1] = prefix_x[i]
        
        answer = []
        for l, r in queries:
            total_sum = prefix_sum[r+1] - prefix_sum[l]
            digit_count = prefix_count[r+1] - prefix_count[l]
            x = (prefix_x[r+1] - prefix_x[l] * pow10[digit_count]) % MOD
            answer.append((x * total_sum) % MOD)
        
        return answer
