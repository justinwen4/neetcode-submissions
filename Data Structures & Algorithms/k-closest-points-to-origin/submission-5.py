class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)

            heapq.heappush(heap, (distance, [x, y]))

        output = []

        for i in range(k):
            distance, coordinates = heapq.heappop(heap)

            output.append(coordinates)

        return output