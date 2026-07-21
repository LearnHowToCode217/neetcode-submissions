# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        k = 0

        pnt1 = pnt2 = dummy
        while curr:
            k += 1
            curr = curr.next

        for i in range(k - n):
            pnt1 = pnt1.next
        pnt1.next = pnt1.next.next
        return dummy.next