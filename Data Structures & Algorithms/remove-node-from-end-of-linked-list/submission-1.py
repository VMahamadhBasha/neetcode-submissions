# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s,h=head,head
        if not head:
            return []
        for i in range(n):
            h=h.next
        if not h:
            return head.next
        while h.next:
            s=s.next
            h=h.next
        s.next=s.next.next
        return head
        