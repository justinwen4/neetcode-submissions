class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        return sorted(list(d.keys()), key = lambda x: d[x], reverse = True)[:k]