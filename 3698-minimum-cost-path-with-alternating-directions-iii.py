import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        INF = float('inf')
        grid_cost = lambda i, j: (i + 1) * (j + 1)
        
        # dist[i][j][p]: p=1 means next action must be odd (right/down), p=0 means even (left/up)
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        start = grid_cost(0, 0)
        dist[0][0][1] = start
        pq = [(start, 0, 0, 1)]
        
        directions = [(1, 0, 'down'), (-1, 0, 'up'), (0, 1, 'right'), (0, -1, 'left')]
        
        while pq:
            d, i, j, p = heapq.heappop(pq)
            if d > dist[i][j][p]:
                continue
            
            # Option 1: wait
            np_, nd = 1 - p, d + penalty[i][j]
            if nd < dist[i][j][np_]:
                dist[i][j][np_] = nd
                heapq.heappush(pq, (nd, i, j, np_))
            
            # Option 2: move to an adjacent cell
            for di, dj, direction in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    allowed = (p == 1 and direction in ('right', 'down')) or \
                              (p == 0 and direction in ('left', 'up'))
                    cost = grid_cost(ni, nj)
                    if not allowed:
                        cost += penalty[i][j]
                    nd2, np2 = d + cost, 1 - p
                    if nd2 < dist[ni][nj][np2]:
                        dist[ni][nj][np2] = nd2
                        heapq.heappush(pq, (nd2, ni, nj, np2))
        
        return min(dist[m-1][n-1][0], dist[m-1][n-1][1])
