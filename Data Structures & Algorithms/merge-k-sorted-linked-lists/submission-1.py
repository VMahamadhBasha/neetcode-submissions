# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i in lists:
            p=i
            while p:
                res.append(p.val)
                p=p.next
        res.sort()
        d=ListNode(0)
        cur=d
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return d.next