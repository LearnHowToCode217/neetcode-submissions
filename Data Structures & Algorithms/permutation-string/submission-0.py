class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)

        k = len(s1)
        l = 0
        count2 = {}
        for r in range(len(s2)): 
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if (r - l +1) > k:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1

            if (r - l +1) == k:
                if count1 == count2:
                    return True
                
        return False


