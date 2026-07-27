"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={None:None}
        p=head
        while p:
            c=Node(p.val)
            d[p]=c
            p=p.next
        p=head
        while p:
            c=d[p]
            c.next=d[p.next]
            c.random =d[p.random]
            p=p.next
        return d[head]