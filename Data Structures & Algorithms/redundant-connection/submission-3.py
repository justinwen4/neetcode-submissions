class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        # [0, 1, 2, 3, 4]

        rank = [1] * (n + 1)


        def find(n):
            if n != par[n]:
                return find(par[n])
            
            return n

        def union(n1, n2):
            p1, p2 = find(n1), find(n2) # find parents

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            
            else:
                rank[p2] += rank[p1]
                par[p1] = p2

            return True

        for n1, n2 in edges:
            if not union(n1, n2): 
                return [n1, n2]
        