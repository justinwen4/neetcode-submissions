class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, req in prerequisites:
            preMap[crs].append(req)

        seen = set()
        def dfs(i):
            if i in seen:
                return False

            if preMap[i] == []:
                return True

            seen.add(i)
            for pre in preMap[i]:
                if not dfs(pre): return False
            
            seen.remove(i)
            preMap[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True

            