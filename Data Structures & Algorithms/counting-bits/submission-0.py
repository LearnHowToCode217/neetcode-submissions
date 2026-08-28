class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            for i in range(32):
                pos = 1 << i
                if pos & num == pos:
                    count += 1
            res.append(count)
        
        return res