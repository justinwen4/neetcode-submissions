# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr
        digit = 0
        leftover = 0

        while l1 or l2 or leftover:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + leftover
            digit = val % 10
            leftover = val // 10

            dummy.next = ListNode(digit)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            dummy = dummy.next

        return curr.next
