# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        l = root
        l_height = 0
        while l:
            l = l.left
            l_height += 1
        
        r = root
        r_height = 0
        while r:
            r = r.right
            r_height += 1
        
        if l_height == r_height:
            return 2**l_height - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
