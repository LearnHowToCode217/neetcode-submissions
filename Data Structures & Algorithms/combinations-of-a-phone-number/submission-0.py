class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        symbol = {'2' : ('a','b','c'),
        '3' : ('d','e','f'), 
        '4' : ('g','h','i'),
        '5' : ('j','k','l'),
        '6' : ('m','n','o'),
        '7' : ('p','q','r','s'),
        '8' : ('t','u','v'),
        '9' : ('w','x','y','z')}

        def backtrack(start, path):
            if not digits:
                return

            if start == len(digits):
                res.append(''.join(path))
                return

            for char in symbol[digits[start]]:
                path.append(char)
                backtrack(start + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res
                

           