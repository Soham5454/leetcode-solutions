class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        flat = [x for row in grid for x in row]
        
        k = k % (m * n)
        
        new_flat = [None] * (m * n)
        for i in range(m * n):
            new_flat[(i + k) % (m * n)] = flat[i]
        
        result = []
        for r in range(m):
            row = new_flat[r * n : (r + 1) * n]
            result.append(row)
        
        return result
