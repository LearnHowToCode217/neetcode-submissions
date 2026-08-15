class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        maximum = nums[0]
        
        for num in nums:
            current = max(num, current + num)
            maximum = max(maximum, current)
        
        return maximum