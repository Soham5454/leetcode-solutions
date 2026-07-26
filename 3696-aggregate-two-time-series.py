import bisect

class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        t1 = [x[0] for x in series1]
        v1 = [x[1] for x in series1]
        t2 = [x[0] for x in series2]
        v2 = [x[1] for x in series2]
        
        timestamps = sorted(set(t1) | set(t2))
        
        result = []
        for t in timestamps:
            i = bisect.bisect_left(t1, t)
            val1 = v1[i] if i < len(t1) else 0
            
            j = bisect.bisect_left(t2, t)
            val2 = v2[j] if j < len(t2) else 0
            
            result.append([t, val1 + val2])
        
        return result
