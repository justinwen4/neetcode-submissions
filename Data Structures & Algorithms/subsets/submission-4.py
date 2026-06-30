class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                subset.append(curr.copy())
                return 

            # include 1
            curr.append(nums[i])
            dfs(i + 1)

            # don't include 1
            curr.pop()
            dfs(i + 1)
            
        dfs(0)
        return subset