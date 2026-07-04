class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        parts = []

        def dfs(i):
            if i == len(nums):
                res.append(parts.copy())
                return

            # keep
            parts.append(nums[i])
            dfs(i + 1)

            # throw
            parts.pop()
            dfs(i + 1)

        dfs(0)
        return res
