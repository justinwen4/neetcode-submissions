class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)

        seen = set()

        def isPossible(i):
            if i in seen:
                return False

            if adjList[i] == []:
                return True

            seen.add(i)
            for pre in adjList[i]:
                if not isPossible(pre): return False

            adjList[i] = []
            seen.remove(i)
            return True


        for i in range(numCourses):
            if not isPossible(i): return False
            
        return True