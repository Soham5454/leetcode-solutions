from typing import List
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        runs = []
        run_start = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            run_start.append(i)
            i = j

        k = len(runs)

        def run_end(idx):
            return run_start[idx] + runs[idx][1]

        def find_run(pos):
            return bisect.bisect_right(run_start, pos) - 1

        ones_prefix = [0] * (n + 1)
        for idx in range(n):
            ones_prefix[idx + 1] = ones_prefix[idx] + (1 if s[idx] == '1' else 0)

        full_ones = ones_prefix[n]   

        gain = [-1] * k
        for idx in range(1, k - 1):
            if runs[idx][0] == '1':
                gain[idx] = runs[idx - 1][1] + runs[idx + 1][1]

        LOG = [0] * (k + 1)
        for idx in range(2, k + 1):
            LOG[idx] = LOG[idx // 2] + 1

        st = [gain[:]]
        p = 1
        while (1 << p) <= k:
            size = k - (1 << p) + 1
            prev = st[p - 1]
            curr = [0] * size
            half = 1 << (p - 1)
            for idx in range(size):
                curr[idx] = max(prev[idx], prev[idx + half])
            st.append(curr)
            p += 1

        def range_max(lo, hi):
            if lo > hi:
                return -1
            p = LOG[hi - lo + 1]
            return max(st[p][lo], st[p][hi - (1 << p) + 1])

        answer = []
        for l, r in queries:
            run_l = find_run(l)
            run_r = find_run(r)

            if run_l == run_r:
                answer.append(full_ones)   
                continue

            left_len = run_end(run_l) - l
            right_len = r - run_start[run_r] + 1

            best = 0

            if run_r == run_l + 1:
                pass
            else:
                lo, hi = run_l + 2, run_r - 2
                best = max(best, range_max(lo, hi))

                j = run_l + 1
                if runs[j][0] == '1':
                    left_neighbor_len = left_len
                    right_neighbor_len = (
                        right_len if j + 1 == run_r else runs[j + 1][1]
                    )
                    best = max(best, left_neighbor_len + right_neighbor_len)

                j2 = run_r - 1
                if j2 != j and runs[j2][0] == '1':
                    left_neighbor_len = (
                        left_len if j2 - 1 == run_l else runs[j2 - 1][1]
                    )
                    right_neighbor_len = right_len
                    best = max(best, left_neighbor_len + right_neighbor_len)

            answer.append(full_ones + best)   

        return answer
