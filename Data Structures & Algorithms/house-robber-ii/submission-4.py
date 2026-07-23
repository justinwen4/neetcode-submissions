class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def robArray(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        max1 = robArray(nums[1:])
        max2 = robArray(nums[:-1])

        return max(max1, max2)