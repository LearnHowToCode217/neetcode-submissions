class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key = lambda x : x[1])
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            
            elif res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
        
        return (len(intervals) - len(res))