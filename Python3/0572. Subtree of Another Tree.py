# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         val = x
#         left = None
#         right = None

class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        
        if not s:
            return False

        def func(s,t):
            if not s and not t:
                return True
            
            if not s or not t:
                return False

            return s.val == t.val and func(s.left,t.left) and func(s.right,t.right) 
                

        return func(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
