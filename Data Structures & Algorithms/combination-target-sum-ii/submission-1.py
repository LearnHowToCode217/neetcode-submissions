class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(total, path, start):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or start == len(candidates):
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                total += candidates[i]
                new_path = path + [candidates[i]]
                backtracking(total, new_path, i + 1)
                new_path.pop()
                total -= candidates[i]
        backtracking(0, [], 0)
        return res