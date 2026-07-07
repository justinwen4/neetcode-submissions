class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()

        def checkCell(r, c):
            if ((r, c) in seen or r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1):
                return

            seen.add((r, c))
            q.append((r, c))
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))

        dist = 0

        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                grid[r][c] = dist

                checkCell(r + 1, c)
                checkCell(r - 1, c)
                checkCell(r, c + 1)
                checkCell(r, c - 1)

            dist += 1


