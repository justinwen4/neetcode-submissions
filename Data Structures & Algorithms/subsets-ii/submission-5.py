class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 

            # All subsets that include nums[i]

            subset.append(nums[i])
            backtrack(i + 1, subset)
            
            # All subsets that don't include nums[i]
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

