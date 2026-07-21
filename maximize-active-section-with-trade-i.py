from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        ones_count = s.count('1')

        groups = [(ch, len(list(g))) for ch, g in groupby(t)]

        best_gain = 0
        for idx in range(1, len(groups) - 1):
            ch, length = groups[idx]
            if ch == '1':
                prev_len = groups[idx - 1][1]
                next_len = groups[idx + 1][1]
                best_gain = max(best_gain, prev_len + next_len)

        return ones_count + best_gain
