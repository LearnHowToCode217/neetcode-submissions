class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(total, path, i):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or i == len(nums):
                return
            
            backtracking(total, path, i + 1)

            new_path = path + [nums[i]]
            total += nums[i]
            backtracking(total, new_path, i)
            new_path.pop()
        
        backtracking(0, [], 0)
        return res