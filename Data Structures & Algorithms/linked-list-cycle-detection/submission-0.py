# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        nums = set()
        while curr:
            if curr in nums:
                return True
            else:
                nums.add(curr)
            
            curr = curr.next
        return False