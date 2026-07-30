class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick numbers
            backtracking(i + 1)

            # Pick numbers
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)
        return res