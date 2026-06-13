# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find middle
        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split it

        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Step 3: Merge them

        first, second = head, prev

        while second:
            ptr1 = first.next
            ptr2 = second.next

            first.next = second
            second.next = ptr1

            first = ptr1
            second = ptr2






