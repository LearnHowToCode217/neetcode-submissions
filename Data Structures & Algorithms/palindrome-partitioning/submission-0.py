class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtracking(start, path):
            if start == len(s):
                res.append(path[:])
                return 

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if isPalindrome(substring, 0, len(substring) - 1):
                    path.append(substring)
                    backtracking(end + 1, path)
                    path.pop()

        backtracking(0, [])
        return res