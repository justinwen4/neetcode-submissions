class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, parts, total):
            if total == target:
                res.append(parts.copy())
                return

            if i == len(nums):
                return

            if total > target:
                return

            parts.append(nums[i])
            dfs(i, parts, total + nums[i])

            parts.pop()
            dfs(i + 1, parts, total)

        dfs(0, [], 0)
        return res



            