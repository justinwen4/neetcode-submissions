"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToNew = {}
        curr = head

        # pass 1: create copies of nodes
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # pass 2: connect next and random pointers
        while curr:
            oldToNew[curr].random = oldToNew[curr.random] if curr.random else None
            oldToNew[curr].next = oldToNew[curr.next] if curr.next else None
            curr = curr.next 

        return oldToNew[head] 
