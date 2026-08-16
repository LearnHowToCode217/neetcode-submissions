class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest, current_end, jump = 0, 0, 0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            if i == current_end and i < len(nums) - 1:
                current_end = farthest
                jump += 1
        
        return jump