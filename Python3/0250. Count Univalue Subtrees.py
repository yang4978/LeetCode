# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def count(self,root):
        if not root:
            return [0,True]
        
        if not root.left and not root.right:
            return [1,True]

        l_count,l = self.count(root.left)
        r_count,r = self.count(root.right)

        if l and r and (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val):
            return [1+l_count+r_count,True]
        else:
            return [l_count+r_count,False]

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        return self.count(root)[0]
        
