class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            val = (l+r) // 2
            if nums[val] > nums[r]:
                l = val + 1
            elif nums[val] <= nums[r]:
                r = val 
            
        return nums[l]