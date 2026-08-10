class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) < 2:
            return max(nums)

        arr = [nums[0], max(nums[1], nums[0])]

        for i in range(2, len(nums)):
            current = max(arr[1], arr[0] + nums[i])
            arr[0] = arr[1] 
            arr[1] = current

        return max(arr)