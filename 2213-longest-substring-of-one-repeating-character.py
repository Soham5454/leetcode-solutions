from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        starts = SortedList()
        run_char = {}
        lengths = SortedList()

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            starts.add(i)
            run_char[i] = s[i]
            lengths.add(j - i)
            i = j

        def get_run(idx):
            pos = starts.bisect_right(idx) - 1
            l = starts[pos]
            pos2 = pos + 1
            r = starts[pos2] if pos2 < len(starts) else n
            return l, r

        def remove_run(l, r):
            starts.remove(l)
            lengths.remove(r - l)
            del run_char[l]

        def add_run(l, r, c):
            starts.add(l)
            lengths.add(r - l)
            run_char[l] = c

        result = []
        for c, idx in zip(queryCharacters, queryIndices):
            if s[idx] != c:
                l, r = get_run(idx)
                old_char = run_char[l]
                remove_run(l, r)
                if idx > l:
                    add_run(l, idx, old_char)
                if idx + 1 < r:
                    add_run(idx + 1, r, old_char)

                s[idx] = c

                L, R = idx, idx + 1

                if idx == l and l > 0:
                    pl = starts[starts.bisect_left(l) - 1]
                    if run_char[pl] == c:
                        remove_run(pl, l)
                        L = pl

                if idx + 1 == r and r < n:
                    _, rr = get_run(r)
                    if run_char[r] == c:
                        remove_run(r, rr)
                        R = rr

                add_run(L, R, c)

            result.append(lengths[-1])

        return result
