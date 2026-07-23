class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(res, opened, closed):
            if closed > opened or opened > n or closed > n:
                return

            if len(res) == n * 2:
                ret.append(''.join(res))

            res.append('(')
            dfs(res, opened + 1, closed)

            res.pop()
            res.append(')')
            dfs(res, opened, closed + 1)
            res.pop()
            
        dfs([], 0, 0)
        return ret

            