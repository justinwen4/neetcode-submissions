class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        output = []
        visit, cycle = set(), set()
        # a course has three possible states
        # 1. it has been added to output
        # 2. it has not been added to output, but we are checking for cycle
        # 3. it has not been added to output or cycle

        def dfs(i):
            if i in cycle:
                return False

            if i in visit:
                return True

            cycle.add(i)
            for pre in preMap[i]:
                if not dfs(pre): 
                    return False

            cycle.remove(i)
            visit.add(i)
            output.append(i)

            return True


        for course in range(numCourses):
            if not dfs(course): return []

        return output