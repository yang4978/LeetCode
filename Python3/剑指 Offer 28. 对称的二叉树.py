# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirror(self, r1, r2):
        if not r1 and not r2:
            return True
        
        elif not r1 or not r2:
            return False

        elif r1.val == r2.val:
            return self.mirror(r1.left, r2.right) and self.mirror(r1.right, r2.left)
        
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root, root)
