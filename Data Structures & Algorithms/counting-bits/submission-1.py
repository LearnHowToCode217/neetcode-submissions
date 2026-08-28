class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for num in range(1, n+1):
            res[num] = res[num & (num-1)] + 1
        
        return res