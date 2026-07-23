# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        max_sum = 0
        p1 = head
        p2 = prev
        while p2:
            max_sum = max(max_sum, p1.val + p2.val)
            p1 = p1.next 
            p2 = p2.next 
        return max_sum

