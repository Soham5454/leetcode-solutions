class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = set()
        stack = [1]
        visited.add(1)
        min_score = float('inf')
        
        while stack:
            city = stack.pop()
            for neighbor, dist in graph[city]:
                min_score = min(min_score, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return min_score
