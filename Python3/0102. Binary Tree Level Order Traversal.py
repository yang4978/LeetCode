# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [(root,1)]
        res = []

        while queue:
            node,layer = queue.pop(0)
            if node:
                if layer == len(res):
                    res[layer-1].append(node.val)
                else:
                    res.append([node.val])
                queue.append((node.left,layer+1))
                queue.append((node.right,layer+1))
        
        return res
