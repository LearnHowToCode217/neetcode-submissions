class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if (r < 0 or 
            c < 0 or 
            r >= ROWS or 
            c >= COLS or 
            grid[r][c] != 1):
                return
            
            grid[r][c] = 0
            nonlocal count 
            count += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = 0
                    dfs(r, c)
                    max_area = max(max_area, count)
        
        return max_area