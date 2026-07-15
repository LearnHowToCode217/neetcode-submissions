class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            distance = r - l
            Area = min(heights[r],heights[l]) * distance
            largest = max(Area, largest)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return largest