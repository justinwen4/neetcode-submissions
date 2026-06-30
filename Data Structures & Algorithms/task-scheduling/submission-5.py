class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            if task not in count:
                count[task] = 0

            count[task] += 1

        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

