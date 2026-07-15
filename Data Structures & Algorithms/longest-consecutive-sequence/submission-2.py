class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        longest = 0
        curr = 1
        prev = None
        for num in nums:
            if prev is not None and num == prev + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
                longest = max(longest, curr)
            prev = num
            
        return longest