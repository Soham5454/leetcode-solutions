class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rsum(a, b):
            return prefix[b + 1] - prefix[a]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                lo, hi = i, j - 1
                k0 = i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    ls = rsum(i, mid)
                    rs = rsum(mid + 1, j)
                    if ls <= rs:
                        k0 = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0
                if k0 >= i:
                    best = max(best, maxL[i][k0])
                    ls0 = rsum(i, k0)
                    rs0 = rsum(k0 + 1, j)
                    if ls0 == rs0:
                        best = max(best, rs0 + dp[k0 + 1][j])
                if k0 + 1 <= j - 1:
                    best = max(best, maxR[k0 + 2][j])

                dp[i][j] = best
                maxL[i][j] = max(maxL[i][j - 1], rsum(i, j) + dp[i][j])
                maxR[i][j] = max(maxR[i + 1][j], rsum(i, j) + dp[i][j])

        return dp[0][n - 1]
