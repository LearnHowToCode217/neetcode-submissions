class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: [index, height]
        heights.append(0)
        max_area = 0
        for i, height in enumerate(heights):
            curr_ind = i
            while stack and height < stack[-1][1]:
                curr_ind, h = stack.pop()
                width = i - curr_ind
                area = width * h 
                max_area = max(max_area, area)

            stack.append([curr_ind, height])   

        return max_area