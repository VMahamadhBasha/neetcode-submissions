# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=None
        if not head :
            return None
        p=head
        while p:
            head=head.next
            p.next=prev
            prev=p
            p=head
        return prev