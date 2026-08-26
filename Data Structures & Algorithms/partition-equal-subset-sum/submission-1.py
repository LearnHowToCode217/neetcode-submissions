class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total / 2
        if total % 2 != 0:
            return False
        
        def dfs(i, currSum):
            if currSum == target:
                return True
            if i == len(nums):
                return False    
            return dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)
            
            
            
        return dfs(0, 0)