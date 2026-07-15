class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        type = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in type:
                if stack and stack[-1] == type[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False