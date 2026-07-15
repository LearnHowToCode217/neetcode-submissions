class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur, best  = 0, 0, len(nums) + 1
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                best = min(best, r - l + 1)
                cur -= nums[l]
                l += 1
            
        return 0 if best == len(nums) + 1 else best
                