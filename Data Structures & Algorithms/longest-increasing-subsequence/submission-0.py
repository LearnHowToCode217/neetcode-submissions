class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [1] * len(nums)
        for i in range(len(L)):
            subproblem = [L[k] for k in range(i) if nums[k] < nums[i]]
            L[i] = 1 + max(subproblem, default = 0)
        return max(L, default = 0)