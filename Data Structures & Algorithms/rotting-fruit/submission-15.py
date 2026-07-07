class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        def addRotten(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r == row or c == col or grid[r][c] != 1):
                return

            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0 
        
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                addRotten(r + 1, c)
                addRotten(r - 1, c)
                addRotten(r, c + 1)
                addRotten(r, c - 1)

            time += 1

        return time - 1 if fresh == 0 else -1

