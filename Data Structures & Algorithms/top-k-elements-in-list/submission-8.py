class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        my_list = sorted(list(counts.keys()), key = lambda x : counts[x], reverse = True)

        return my_list[:k]