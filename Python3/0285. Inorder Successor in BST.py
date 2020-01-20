# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                if not res or res.val > root.val:
                    res = root
                root = root.left
        
        return res
