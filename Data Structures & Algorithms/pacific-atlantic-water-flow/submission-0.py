class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r < 0 or r >= ROW or
                c < 0 or c >= COL or
                (r, c) in visited):
                return

            visited.add((r, c))

            if r + 1 < ROW and heights[r + 1][c] >= heights[r][c]:
                dfs(r + 1, c, visited)

            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfs(r - 1, c, visited)

            if c + 1 < COL and heights[r][c + 1] >= heights[r][c]:
                dfs(r, c + 1, visited)

            if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfs(r, c - 1, visited)

        # Pacific Ocean: top row + left column
        for c in range(COL):
            dfs(0, c, pacific)

        for r in range(ROW):
            dfs(r, 0, pacific)

        # Atlantic Ocean: bottom row + right column
        for c in range(COL):
            dfs(ROW - 1, c, atlantic)

        for r in range(ROW):
            dfs(r, COL - 1, atlantic)

        return [[r, c] for r in range(ROW)
                       for c in range(COL)
                       if (r, c) in pacific and (r, c) in atlantic]