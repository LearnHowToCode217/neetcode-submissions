class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(total, path, start):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or start == len(candidates) :
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                total += candidates[i]
                path.append(candidates[i])
                backtracking(total, path, i + 1)
                path.pop()
                total -= candidates[i]
        
        backtracking(0, [], 0)
        return res