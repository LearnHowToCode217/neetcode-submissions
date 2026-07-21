# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr1 = head1 = slow.next
        slow.next = None
        prev = None
        while curr1:
            head1 = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = head1

        head1 = prev

        while head and head1:
            curr = head.next
            curr1 = head1.next

            head.next = head1
            head1.next = curr

            head = curr
            head1 = curr1
            