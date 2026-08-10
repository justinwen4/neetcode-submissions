class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        def robHouse(nums):
            if len(nums) == 0:
                return 0

            if len(nums) < 2:
                return max(nums)

            arr = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                curr = max(arr[1], arr[0] + nums[i])
                arr[0] = arr[1]
                arr[1] = curr

            return max(arr)

        return max(robHouse(nums[:-1]), robHouse(nums[1:]))