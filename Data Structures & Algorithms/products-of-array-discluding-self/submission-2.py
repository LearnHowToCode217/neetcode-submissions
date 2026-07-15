class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * (len(nums) + 1)
        post = [1] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pre[i] = pre[i-1] * nums[i-1]
            post[-(i+1)] = post[-i] * nums[-i]
        
        for num in range(len(nums)):
            nums[num] = post[num+1] * pre[num]
        return nums