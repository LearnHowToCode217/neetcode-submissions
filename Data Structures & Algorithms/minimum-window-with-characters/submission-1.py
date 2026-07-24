class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = float('inf')
        l, start, valid = 0, 0, 0
        need = {}
        window = {}

        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)
        
        for r in range(len(s)):
            if s[r] in need :
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == need[s[r]]:
                    valid += 1
                
                while valid == len(need):
                    if r - l + 1 < length:
                        length = min(length, r - l + 1)
                        start = l

                    d = s[l]
                    if d in need:
                        if window[d] == need[d]:
                            valid -= 1
                        window[d] -= 1 
                    
                    l += 1
        if length == float('inf'):
            return ''
        return s[start:start + length]
                        