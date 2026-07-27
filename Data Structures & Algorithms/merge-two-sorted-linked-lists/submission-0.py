# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r1=[]
        p=list1
        while p:
            r1.append(p.val)
            p=p.next
        p=list2
        while p:
            r1.append(p.val)
            p=p.next
        r1.sort()
        d=ListNode(0)
        cur=d
        for i in r1:
            cur.next=ListNode(i)
            cur=cur.next
        return d.next

        