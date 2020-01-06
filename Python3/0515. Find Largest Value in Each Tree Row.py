# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            max_value = -float('inf')
            for _ in range(len(queue)):
                node = queue.pop(0)
                
                max_value = max(max_value,node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            res.append(max_value)
        return res

        # if not root:
        #     return []

        # queue = [(root,1)]
        # res = []

        # while queue:
        #     node,layer = queue.pop(0)
            
        #     if layer>len(res):
        #         res.append(node.val)
        #     else:
        #         res[layer-1] = max(res[layer-1],node.val)
            
        #     if node.left:
        #         queue.append((node.left,layer+1))
            
        #     if node.right:
        #         queue.append((node.right,layer+1))
        
        # return res
