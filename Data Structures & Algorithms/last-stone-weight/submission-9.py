class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            val1 = -(heapq.heappop(heap))
            val2 = -(heapq.heappop(heap))

            if val1 > val2:
                new = val1 - val2
                heapq.heappush(heap, -new)

        if len(heap) == 1:
            return -(heap[0])

        else:
            return 0            
