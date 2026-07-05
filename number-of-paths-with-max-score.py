class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        board = [list(row) for row in board]
        
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)  # base case: sum 0, exactly 1 way to "be" at S
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X':
                    continue
                if i == n-1 and j == n-1:
                    continue
                
                best_sum, best_count = -1, 0
                
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n:
                        s, c = dp[ni][nj]
                        if c > 0:
                            if s > best_sum:
                                best_sum, best_count = s, c   # new strictly better sum → reset count
                            elif s == best_sum:
                                best_count += c                # tie → accumulate ways
                
                if best_count == 0:
                    dp[i][j] = (-1, 0)
                else:
                    val = 0 if board[i][j] in ('E', 'S') else int(board[i][j])
                    dp[i][j] = (best_sum + val, best_count % MOD)
        
        max_sum, count = dp[0][0]
        if count == 0:
            return [0, 0]
        return [max_sum, count]
