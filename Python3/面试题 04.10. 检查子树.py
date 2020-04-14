# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSame(self,t1,t2):
        if not t1 and not t2:
            return True
        
        if not t1 or not t2:
            return False
        
        return t1.val == t2.val and self.isSame(t1.left,t2.left) and self.isSame(t1.right,t2.right)

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1:
            return False
        
        return self.isSame(t1,t2) or self.checkSubTree(t1.left,t2) or self.checkSubTree(t1.right,t2)
