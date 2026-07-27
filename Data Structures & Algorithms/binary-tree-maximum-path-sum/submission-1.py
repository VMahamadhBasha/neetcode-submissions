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
            s=dfs(r.right)
            l,s=max(0,l),max(0,s)
            res[0]=max(res[0],r.val+l+s)
            return r.val+max(l,s)
        dfs(r)
        return res[0]