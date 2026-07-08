class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, ocean, prevHeight):
            if (r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight or (r, c) in ocean):
                return
            
            ocean.add((r, c))

            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        ret = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    ret.append([r, c])

        return ret

        