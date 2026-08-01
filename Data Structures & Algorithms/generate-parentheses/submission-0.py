class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [] 
        def backtracking(Nopen, Nclose):
            if Nopen == Nclose == n:
                res.append(''.join(stack))
                return
            
            if Nopen < n :
                stack.append('(')
                backtracking(Nopen + 1, Nclose)
                stack.pop()

            if Nclose < Nopen:
                stack.append(')')
                backtracking(Nopen, Nclose + 1)
                stack.pop()
        
        backtracking(0,0)
        return res

            

