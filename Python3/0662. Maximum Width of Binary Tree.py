# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root,0)]
        res = 0
        while queue:
            arr = []
            for _ in range(len(queue)):
                node,pos = queue.pop(0)
                arr.append(pos)
                if node.left:
                    queue.append((node.left,pos*2))
                if node.right:
                    queue.append((node.right,pos*2+1))
            
            res = max(res,1+arr[-1]-arr[0])
        
        return res
