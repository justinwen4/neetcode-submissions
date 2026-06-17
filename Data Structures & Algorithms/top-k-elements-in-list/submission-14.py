class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        freqs = {}

        for num in nums:
            if num not in freqs:
                freqs[num] = 0

            freqs[num] += 1

        for key, value in freqs.items():
            buckets[value].append(key)

        output = []

        for i in reversed(range(len(buckets))):
            if len(buckets[i]) == 0:
                continue
            
            for item in buckets[i]:
                output.append(item)

                if len(output) == k:
                    return output
