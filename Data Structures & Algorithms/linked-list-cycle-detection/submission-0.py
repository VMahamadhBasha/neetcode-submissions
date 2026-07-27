# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,f=head,head
        c=0
        while f.next and f.next.next:
            f=f.next.next
            s=s.next
            if f.val==s.val:
                return True
        return False 