# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def height(node):
            if not node:
                return 0
            return max(height(node.left),height(node.right))+1
        
        if not root:
            return None
        
        l = height(root.left)
        r = height(root.right)

        if l==r:
            return root
        
        if l>r:
            return self.subtreeWithAllDeepest(root.left)
        
        if l<r:
            return self.subtreeWithAllDeepest(root.right)
