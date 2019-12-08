# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [(root,1)]
        res = []
        l = 0

        while queue:
            node,layer = queue.pop(0)
            if layer>l:
                res.append(node.val)
                l += 1
            else:
                res[-1] = node.val

            if node.left:
                queue.append((node.left,layer+1))
            
            if node.right:
                queue.append((node.right,layer+1))

        return res
