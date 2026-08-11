class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        def bfs(r, c):
            nonlocal fresh
            if (r < 0 or 
                c < 0 or 
                r >= ROWS or
                c >= COLS or 
                grid[r][c] == 0 or 
                (r, c) in visit):
                    return

            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1

            q.append([r, c])
            visit.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        
        minute = 0
        while q and fresh >0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            minute += 1
        
        if fresh > 0 :
            return -1
        
        return minute
                
                