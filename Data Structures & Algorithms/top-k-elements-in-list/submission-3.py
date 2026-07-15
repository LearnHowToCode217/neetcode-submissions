class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        Freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hashtable[num] = 1 + hashtable.get(num, 0)
        
        for i, val in hashtable.items():
            Freq[val].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in Freq[i]:
                res.append(num)
                if len(res) == k:
                    return res