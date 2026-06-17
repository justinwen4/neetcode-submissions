class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Product of elements to left
        output = [0] * len(nums)
        left = 1

        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]

        # Step 2: Product of elements to right
        right = 1
        for i in reversed(range(len(nums))):
            output[i] *= right
            right *= nums[i]

        return output        