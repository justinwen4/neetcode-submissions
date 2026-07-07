class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minVal = self.findMinValue(nums)
        left = self.binarySearch(nums, target, 0, minVal - 1)
        right = self.binarySearch(nums, target, minVal, len(nums) - 1)

        return max(left, right)


    def findMinValue(self, nums):
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return 0

        if nums[left] < nums[right]:
            return 0

        while left < right:
            # [3, 4, 5, 1, 2]
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    def binarySearch(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1

