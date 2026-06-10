class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for freq in reversed(range(len(buckets))):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
            