class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total / 2
        memo = {}
        if total % 2 != 0:
            return False
        
        def dfs(i, currSum):
            if currSum == target:
                return True
            if i == len(nums) or currSum > target:
                return False
            if (i, currSum) in memo:
                return memo[(i,currSum)]
            memo[(i, currSum)] = dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)

            return memo[(i, currSum)]
        
        return dfs(0, 0)
              