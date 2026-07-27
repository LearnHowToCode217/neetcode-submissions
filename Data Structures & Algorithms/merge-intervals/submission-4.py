class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merge = []
        i = 0
        while i < len(intervals):
            if not merge:
                merge.append(intervals[i])

            elif merge[-1][1] >= intervals[i][1]:
                i += 1
                continue

            elif merge[-1][1] >= intervals[i][0]:
                merge[-1][1] = intervals[i][1]
            
            else:
                merge.append(intervals[i])
            
            i += 1
        
        return merge
