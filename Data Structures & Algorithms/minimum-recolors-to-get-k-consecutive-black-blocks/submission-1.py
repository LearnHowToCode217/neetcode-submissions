class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        total_white = blocks[:].count('W')
        min_w = total_white
        

        for r in range(k, len(blocks)):
            l = r - k
            count_white = blocks[l:r].count('W')
            min_w = min(min_w, count_white)
        
        return min_w

        
            
