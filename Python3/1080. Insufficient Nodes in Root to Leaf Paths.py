# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def prune(self,root,limit):
        l,r = 0,0

        if root.left:
            root.left,l = self.prune(root.left, limit-root.val)
        
        if root.right:
            root.right,r = self.prune(root.right, limit-root.val)
        
        if not root.left and not root.right:
            return (root,0) if root.val >= limit and l==0 and r==0 else (None,1)
        
        return (root,0)

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        root,t = self.prune(root,limit)
        return root
