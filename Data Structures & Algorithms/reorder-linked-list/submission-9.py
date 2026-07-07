# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        second = slow.next
        slow.next = None
        curr, prev = second, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        #join
        while second:
            ptr1 = head.next
            ptr2 = second.next

            head.next = second
            second.next = ptr1

            head = ptr1
            second = ptr2
        
        
        