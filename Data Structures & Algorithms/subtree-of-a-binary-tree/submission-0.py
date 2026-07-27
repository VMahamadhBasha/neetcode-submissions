# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], sb: Optional[TreeNode]) -> bool:
        if not sb:
            return True
        if not r:
            return False
        def same(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val ==b.val and  same(a.left,b.left) and same(a.right,b.right)
        return same(r,sb) or self.isSubtree(r.left,sb) or self.isSubtree(r.right,sb)
