# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res=[]
        def tree(root):
            if not root:
                res.append('null')
                return
            res.append(root.val)
            tree(root.left)
            tree(root.right)
            return res
        p1=tree(p)
        print(p1)
        res=[]
        def tree2(root):
            if not root:
                res.append('null')
                return 
            res.append(root.val)
            tree2(root.left)
            tree2(root.right)
            return res
        p2=tree2(q)
        print(p2)
        return p1==p2
        """
        p2=tree2(q)
        print(p1,p2)
        if len(p1)!=len(p2):
            return False
        for i in range(len(p1)):
            if p1[i]!=p2[i]:
                return False
        return True
        """