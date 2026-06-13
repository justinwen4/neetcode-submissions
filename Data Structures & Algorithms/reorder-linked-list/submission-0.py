# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # Find middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next # why
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge two halves

        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
