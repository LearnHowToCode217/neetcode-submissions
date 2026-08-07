import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        for num in range(k):
            largest_kth = heapq.heappop(nums)
        
        return -largest_kth