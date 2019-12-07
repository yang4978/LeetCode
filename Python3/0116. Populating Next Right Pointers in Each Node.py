"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        left = root.left
        right = root.right
        
        while left:
            left.next = right
            left = left.right
            right = right.left
        
        self.connect(root.left)
        self.connect(root.right)

        return root

        # if not root:
        #     return root

        # queue = [(root,0)]

        # while queue:
        #     node,layer = queue.pop(0)
        #     if not queue or queue[0][1]!=layer:
        #         node.next = None
        #     else:
        #         node.next = queue[0][0]
            
        #     if node.left:
        #         queue.append((node.left,layer+1))
            
        #     if node.right:
        #         queue.append((node.right,layer+1))
        
        # return root
