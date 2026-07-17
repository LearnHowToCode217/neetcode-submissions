class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')' : '(', ']':'[','}':'{'}
        for c in s:
            if c in brackets:
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
                