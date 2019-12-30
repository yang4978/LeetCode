# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return (not root.left or (root.left.val==root.val and self.isUnivalTree(root.left))) and (not root.right or (root.right.val==root.val and self.isUnivalTree(root.right)))

        # l = True
        # r = True

        # if root.left:
        #     if root.left.val == root.val:
        #         l = self.isUnivalTree(root.left)
        #     else:
        #         l = False
        
        # if root.right:
        #     if root.right.val == root.val:
        #         r = self.isUnivalTree(root.right)
        #     else:
        #         r = False
        
        # return l and r
