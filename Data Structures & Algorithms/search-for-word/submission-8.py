class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            
            # need to check three conditions
            # 1. outside of board
            # 2. not the same letter
            # 3. already seen path
            if (row < 0 or col < 0 or row >= r or col >= c or word[i] != board[row][col] or (row, col) in path):
                return False

            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or 
            dfs(row - 1, col, i + 1) or 
            dfs(row, col + 1, i + 1) or 
            dfs(row, col - 1, i + 1))
            
            path.remove((row, col))
            return res

        for row in range(r):
            for col in range(c):
                if dfs(row, col, 0): return True

        return False
