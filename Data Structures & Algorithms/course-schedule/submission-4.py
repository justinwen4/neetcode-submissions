class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False

            if prevMap[crs] == []:
                return True

            visitSet.add(crs)
            for prev in prevMap[crs]:
                if not dfs(prev): return False
            visitSet.remove(crs)
            prevMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True