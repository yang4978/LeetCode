# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            length = 1
            if node.left:
                l = dfs(node.left)
                if node.left.val - node.val == 1:
                    length = max(length,l+1)
            if node.right:
                r = dfs(node.right)
                if node.right.val - node.val == 1:
                    length = max(length, r+1)
            
            res = max(res,length)

            return length
        
        res = 0
        dfs(root)
        return res

    # def traversal(self,root):
    #     if not root:
    #         return 1
        
    #     t = 1

    #     if root.left:
    #         tl = self.traversal(root.left)
    #         if root.left.val-root.val==1:
    #             t = max(t,tl+1)
        
    #     if root.right:
    #         tr = self.traversal(root.right)
    #         if root.right.val-root.val==1: 
    #             t = max(t,tr+1)

    #     self.res = max(self.res,t)

    #     return t

    # def longestConsecutive(self, root: TreeNode) -> int:
    #     self.res = 0
    #     self.traversal(root)
    #     return self.res
