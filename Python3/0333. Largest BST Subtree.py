# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNode(self,root):
        if not root:
            return [0,float('inf'),-float('inf')]
              
        l = self.countNode(root.left)
        r = self.countNode(root.right)

        if l[2]<root.val<r[1]:
            return [1+l[0]+r[0],min(l[1],root.val),max(r[2],root.val)]

        return [max(l[0],r[0]),-float('inf'),float('inf')]
    
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.countNode(root)
        
        return res[0]
