class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        row, col = len(grid), len(grid[0])
        max_island_size = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
            r >= row or c >= col or
            (r, c) in seen or grid[r][c] == 0):
                return 0

            seen.add((r, c))

            return (1 + 
            dfs(r + 1, c) +
            dfs(r - 1, c) + 
            dfs(r, c + 1) + 
            dfs(r, c - 1)  
            )

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in seen:
                    curr_island_size = dfs(r, c)
                    max_island_size = max(max_island_size, curr_island_size)
        
        return max_island_size
