# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle

        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half

        second = slow
        save = second.next
        second.next = None
        prev, curr = None, save

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # join the linked lists

        while second:
            node1 = head.next
            node2 = second.next

            head.next = second
            second.next = node1

            head = node1
            second = node2