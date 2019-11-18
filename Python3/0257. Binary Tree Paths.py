# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []

        stack = [(root,str(root.val))]
        while(stack):
            node,temp = stack.pop()
            if not node.left and not node.right:
                res.append(temp)
            
            if node.left:
                stack.append((node.left,temp+'->'+str(node.left.val)))
            
            if node.right:
                stack.append((node.right,temp+'->'+str(node.right.val)))
        
        return res
