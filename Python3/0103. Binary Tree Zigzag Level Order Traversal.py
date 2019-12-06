# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = [(root,1)]
        res = []
        l = 0

        while queue:
            node,layer = queue.pop(0)
            if layer>l:
                res.append([node.val])
                l += 1
            else:
                res[layer-1].append(node.val)
            
            if node.left:
                queue.append((node.left,layer+1))
            
            if node.right:
                queue.append((node.right,layer+1))

        for i in range(1,l,2):
            res[i].reverse()

        return res
