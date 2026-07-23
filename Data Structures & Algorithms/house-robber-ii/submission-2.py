class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        numsList1 = nums[:-1]
        numsList2 = nums[1:]

        max1 = 0
        max2 = 0

        rob1, rob2 = 0, 0

        for num in numsList1:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        max1 = rob2

        rob1, rob2 = 0, 0

        for num in numsList2:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        max2 = rob2

        return max(max1, max2)
