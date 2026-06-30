class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        if not heap:
            return 0

        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            if val1 == val2:
                continue

            if val2 < val1:
                heapq.heappush(heap, -(val1 - val2))

        if heap:
            return -heap[0]
        else:
            return 0