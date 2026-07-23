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
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            max_sum = max(max_sum, v1 + v2)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return max_sum

