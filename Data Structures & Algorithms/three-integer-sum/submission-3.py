class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        list = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r :
                if -val < nums[l] + nums[r]:
                    r -= 1
                elif -val > nums[l] + nums[r]:
                    l += 1
                else:
                    list.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return list

