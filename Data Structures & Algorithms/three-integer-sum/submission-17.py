class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = n + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[left], nums[right], n])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                if total < 0:
                    left += 1
                
                if total > 0:
                    right -= 1

        return result
