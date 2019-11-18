# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool: 
        if (not root):
            return False
        
        stack = [(root,sum-root.val)]

        while stack:
            node, temp = stack.pop()
            if(not node.left and not node.right and temp==0):
                return True
            if node.left:
                stack.append((node.left,temp-node.left.val))
            if node.right:
                stack.append((node.right,temp-node.right.val))
        
        return False

        # if(root==None):
        #     return False
        # sum -= root.val
        # if(root.left==None and root.right==None):
        #     return sum==0
        
        # return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
