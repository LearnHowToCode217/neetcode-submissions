class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0 
        nums = sorted(nums)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        return slow