class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            total_time = 0
            val = (l+r) // 2
            for p in piles:
                total_time += math.ceil(p/val)
            if total_time > h:
                l = val + 1
            else:
                r = val - 1

        return l