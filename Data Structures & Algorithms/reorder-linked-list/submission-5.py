# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # Step 1: Separate list in half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        curr, prev = second, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        
        # Step 3: Join the two 
        while second:
            ptr1 = head.next
            ptr2 = second.next

            head.next = second
            second.next = ptr1

            head = ptr1
            second = ptr2

