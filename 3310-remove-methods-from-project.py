from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    queue.append(nxt)
        
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))  
        
        return sorted(m for m in range(n) if m not in suspicious)
