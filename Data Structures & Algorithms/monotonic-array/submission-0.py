class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = increasing = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False

        return decreasing or increasing 