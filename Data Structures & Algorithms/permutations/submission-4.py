class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:
                if num in used:
                    continue

                curr.append(num)
                used.add(num)
                dfs(curr)

                curr.pop()
                used.remove(num) 

        dfs([])
        return res

                