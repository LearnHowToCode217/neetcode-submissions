class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Ana = {}
        for word in strs:
            Count = {}
            for i in range(len(word)):
                Count[word[i]] = 1 + Count.get(word[i], 0)
            key = tuple(sorted(Count.items()))
            if key in Ana:
                Ana[key].append(word)
            else:
                Ana[key] = [word]
        return list(Ana.values())
