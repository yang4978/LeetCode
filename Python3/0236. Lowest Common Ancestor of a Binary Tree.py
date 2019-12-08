# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse_tree(node):
            if not node:
                return False
            left = recurse_tree(node.left)
            right = recurse_tree(node.right)
            mid = node==p or node==q

            if left+right+mid>=2:
                self.res = node
            
            return left or right or mid
        recurse_tree(root)
        return self.res
