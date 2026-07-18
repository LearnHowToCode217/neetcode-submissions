class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        stack1 = []
        stack_left, stack_right = [0] * len(height), [0] * len(height)
        water_trap = []
        for r in range(len(height) - 1):
            while stack and height[r] > stack[-1]:
                stack.pop()
            if stack:
                stack_left[r] = stack[-1]
                continue
            stack.append(height[r])
        
        for r1 in range(len(height) - 1, -1, -1):
            while stack1 and height[r1] > stack1[-1]:
                stack1.pop()
            if stack1:
                stack_right[r1] = stack1[-1]
                continue
            stack1.append(height[r1])

        for i in range(len(height)):
            if min(stack_left[i], stack_right[i]) == 0:
                continue
            val = min(stack_left[i], stack_right[i]) - height[i]
            water_trap.append(val)
        return sum(water_trap)