class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for sorted_idx, orig_idx in enumerate(order):
            pos[orig_idx] = sorted_idx

        sorted_nums = [nums[i] for i in order]

        reach = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sorted_nums[j+1] - sorted_nums[i] <= maxDiff:
                j += 1
            reach[i] = j

        LOG = max(1, n.bit_length())
        jump = [[0] * n for _ in range(LOG)]
        jump[0] = reach[:]
        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k-1][jump[k-1][i]]

        answer = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if a > b:
                a, b = b, a
            if a == b:
                answer.append(0)
                continue
            cur = a
            hops = 0
            reachable = True
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < b:
                    hops += 1 << k
                    cur = jump[k][cur]
            if reach[cur] >= b:
                hops += 1
            else:
                reachable = False
            answer.append(hops if reachable else -1)
        return answer
