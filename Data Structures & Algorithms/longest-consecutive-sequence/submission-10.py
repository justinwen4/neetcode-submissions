class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)

        long_sequence = 0

        for num in nums:
            if num - 1 in num_set:
                continue

            i = 1
            while num + 1 in num_set:
                num += 1
                i += 1

            long_sequence = max(long_sequence, i)

        return long_sequence