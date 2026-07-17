class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = {i:[] for i in range(n)}
        for e1, e2 in edges:
            graphMap[e1].append(e2)
            graphMap[e2].append(e1)

        count = 0
        seen = set()

        def dfs(i):
            if i in seen:
                return

            seen.add(i)
            for connection in graphMap[i]:
                dfs(connection)
        
        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)

        return count
                
