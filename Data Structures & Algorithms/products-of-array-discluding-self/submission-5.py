class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] = left
            left = left * nums[i]

        # [1, 1, 2, 8]

        right = 1
        for i in reversed(range(len(nums))):
            output[i] = output[i] * right
            right = right * nums[i]

        return output
        
        
