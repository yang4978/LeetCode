# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def length(node):
            if not node:
                return 0

            l_length = length(node.left)
            l = 0
            if node.left and node.val==node.left.val:
                l = l_length + 1

            r_length = length(node.right)       
            r = 0    
            if node.right and node.val==node.right.val:
                r += r_length + 1

            self.ans = max(self.ans,r+l)
            return max(r,l)
        
        length(root)
        return self.ans
