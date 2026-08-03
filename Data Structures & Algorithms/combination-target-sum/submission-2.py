class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        def backtracking(total, path, i):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or i == len(nums):
                return
            
            total += nums[i]
            path.append(nums[i])
            backtracking(total, path, i)
            path.pop()
            total -= nums[i]

            backtracking(total, path, i + 1)

        backtracking(0, [], 0)
        return res
