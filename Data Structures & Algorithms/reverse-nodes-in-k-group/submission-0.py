# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        if not head:
            return None
        p=head
        while p:
            res.append(p.val)
            p=p.next
        i=0
        r1=[]
        while (i+k)<=len(res):
            r=res[i:i+k]
            r.reverse()
            r1+=r
            i+=k
        r1+=res[i::]
        print(r1)
        d=ListNode(0)
        cur=d
        for i in r1:
            cur.next=ListNode(i)
            cur=cur.next
        return d.next
