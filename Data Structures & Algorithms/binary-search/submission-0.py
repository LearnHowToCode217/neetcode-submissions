class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            val = (l+r) // 2
            if nums[val] == target:
                return val
            elif nums[val] < target:
                l = val + 1
            else:
                r = val - 1
        return -1