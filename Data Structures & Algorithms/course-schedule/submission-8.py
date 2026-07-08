class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a hashmap of courses and prerequisites

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        # dfs function
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

        # iterate through 

        for i in range(numCourses):
            if not dfs(i): return False

        return True