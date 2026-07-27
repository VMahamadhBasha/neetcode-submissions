# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=[]
        if not head:
            return None
        while head:
            st.append(head.val)
            head=head.next
        p=ListNode(0)
        cur=p
        while st:
            cur.next=ListNode(st.pop())
            cur=cur.next
        return p.next
