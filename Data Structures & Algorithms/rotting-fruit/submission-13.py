class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def addRotten(r, c):
            nonlocal fresh

            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1):
                return
            
            q.append((r, c))
            grid[r][c] = 2
            fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
    
        if fresh == 0:
            return 0

        time = 0

        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                grid[r][c] = 2
            
                addRotten(r + 1, c)
                addRotten(r - 1, c)
                addRotten(r, c + 1)
                addRotten(r, c - 1)

            time += 1

        return time - 1 if fresh == 0 else -1
