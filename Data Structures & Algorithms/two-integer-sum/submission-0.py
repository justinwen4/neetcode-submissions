class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n1 in range(len(nums)):
            for n2 in range(n1 + 1, len(nums)):
                if nums[n1] + nums[n2] == target:
                    return [n1, n2]