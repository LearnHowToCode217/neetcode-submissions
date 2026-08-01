class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                
                new_path = path + [num]
                backtracking(new_path)
                new_path.pop()
            
        backtracking([])
        return res