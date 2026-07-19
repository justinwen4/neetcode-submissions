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

                used.add(num)
                curr.append(num)
                dfs(curr)

                used.remove(num)
                curr.pop()                
            
        dfs([])
        return res
