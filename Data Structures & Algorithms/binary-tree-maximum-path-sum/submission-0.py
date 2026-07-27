# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, r: Optional[TreeNode]) -> int:
        res=[r.val]
        def dfs(r):
            if not r:
                return 0
            l=dfs(r.left)
            r1=dfs(r.right)
            l,r1=max(0,l),max(0,r1)
            res[0]=max(res[0],r.val+l+r1)
            return r.val+max(l,r1)
        dfs(r)
        return res[0]