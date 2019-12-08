# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        return root

    # def isAncestor(self,root,node):
    #     if not root:
    #         return False

    #     if root==node:
    #         return True
        
    #     return self.isAncestor(root.left,node) or self.isAncestor(root.right,node)

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if self.isAncestor(root.left,p) and self.isAncestor(root.left,q):
    #         return self.lowestCommonAncestor(root.left,p,q)
        
    #     if self.isAncestor(root.right,p) and self.isAncestor(root.right,q):
    #         return self.lowestCommonAncestor(root.right,p,q)
        
    #     return root
