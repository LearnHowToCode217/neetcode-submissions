class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Ana = {}
        for word in strs:
            Count = [0] * 26
            for i in word:
                val = ord(i) - ord('a')
                Count[val] += 1
            key = tuple(Count)
            if key in Ana:
                Ana[key].append(word)
            else:
                Ana[key] = [word]
        return list(Ana.values())