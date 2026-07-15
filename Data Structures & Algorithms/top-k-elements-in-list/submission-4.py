class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        Freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for i, val in count.items():
            Freq[val].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in Freq[i]:
                if len(res) < k:
                    res.append(num)
        return res