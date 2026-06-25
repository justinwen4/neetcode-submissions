# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        result = []

        while q:
            rightSide = None
            length = len(q)

            for i in range(length):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                result.append(rightSide.val)

        return result
