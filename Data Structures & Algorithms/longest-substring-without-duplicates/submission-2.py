class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, r, best = 0, 0, 0
        while r <= len(s) - 1:
            if s[r] in hashset:
                best = max(best,len(hashset))
                hashset.remove(s[l])
                l += 1
            else:
                hashset.add(s[r])
                r += 1
                best = max(best,len(hashset))
        return best
