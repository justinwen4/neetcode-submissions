class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            adjList[u].append((v, w))

        # build the adjacency list


        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        # initialize minHeap of time 0 and k starting node

        t = 0 
        seen = set()

        # initialize time variable and set to track seen nodes

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in seen:
                continue

            seen.add(n1)
            # make sure we maintain minimum

            t = max(t, w1) # update time

            for n2, w2 in adjList[n1]:
                heapq.heappush(minHeap, (w2 + w1, n2))

        return t if len(seen) == n else -1