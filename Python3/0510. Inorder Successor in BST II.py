"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            
            return node

        while node.parent and node == node.parent.right:
            node = node.parent
        
        return node.parent

        # p = node.val

        # while node.parent:
        #     node = node.parent

        # res = None

        # while node:
        #     if p >= node.val:
        #         node = node.right
        #     else:
        #         if not res or res.val>node.val:
        #             res = node

        #         node = node.left
        
        # return res
