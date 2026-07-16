class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in range(len(operations)):
            if operations[c] not in ["+", "D", "C"]:
                stack.append(int(operations[c]))
            elif operations[c] == '+':
                stack.append(stack[-1] + stack[-2])
            elif operations[c] == 'C':
                stack.pop()
            else:
                stack.append(stack[-1] * 2)
        return sum(stack)