# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i in range(len(lists)):
            p=lists[i]
            while p:
                res.append(p.val)
                p=p.next
        res.sort()
        print(res)
        d=ListNode(0)
        cur=d
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return d.next