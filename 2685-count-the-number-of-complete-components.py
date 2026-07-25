class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(adj[node])
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    sub_nodes, sub_edges = dfs(neighbor)
                    nodes += sub_nodes
                    edge_count += sub_edges
            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)
                edge_count //= 2
                if edge_count == nodes * (nodes - 1) // 2:
                    count += 1

        return count
