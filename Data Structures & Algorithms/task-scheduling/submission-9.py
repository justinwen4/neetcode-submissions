class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqTasks = {}
        for task in tasks:
            if task not in freqTasks:
                freqTasks[task] = 0
            freqTasks[task] += 1

        heap = [-num for num in freqTasks.values()]
        heapq.heapify(heap)

        q = deque()

        cycles = 0

        while heap or q:
            cycles += 1

            if heap:
                task = heapq.heappop(heap)
                task += 1

                if task != 0:
                    q.append((task, cycles + n))

            if q and q[0][1] == cycles:
                task, _ = q.popleft()
                heapq.heappush(heap, task)
        return cycles
