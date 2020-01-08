# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self,root):
        if not root:
            return [1,1]
        
        neg = 1
        pos = 1

        if root.left:
            nl,pl = self.traversal(root.left)
            if root.val - root.left.val == 1:
                pos = max(pos,pl+1)
            elif root.val - root.left.val == -1:
                neg = max(neg,nl+1)
        
        if root.right: 
            nr,pr = self.traversal(root.right)
            if root.val - root.right.val == 1:
                pos = max(pos,pr+1)
            elif root.val-root.right.val == -1:
                neg = max(neg,nr+1)

        self.res = max(self.res,pos,neg,pos+neg-1)

        return [neg,pos] 
    
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        self.traversal(root)
        return self.res
