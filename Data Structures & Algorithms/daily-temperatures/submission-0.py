class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair : [temp, index]
        res = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([val, i])
        return res