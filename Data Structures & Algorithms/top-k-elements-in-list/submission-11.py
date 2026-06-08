class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        
        ret = []

        for i in reversed(range(len(buckets))):
            for num in buckets[i]:
                ret.append(num)

                if len(ret) == k:
                    return ret


            