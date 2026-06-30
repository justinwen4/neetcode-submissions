class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ret = 0

        while k > 0:
            k -= 1
            ret = heapq.heappop(heap)

        return -ret
