"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def helper(node):
            nonlocal first,last
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
            
                last = node

                helper(node.right)
        
        if not root:
            return None
        
        first = None
        last = None
        helper(root)
        last.right = first
        first.left = last
        return first

        # if not root:
        #     return None

        # head = Node(-1)

        # stack = []

        # while root:
        #     stack.append(root)
        #     root = root.left
        
        # pre = head
        # while stack:
        #     cur = stack.pop()
        #     node = cur.right
        #     while node:
        #         stack.append(node)
        #         node = node.left
            
        #     pre.right = cur
        #     cur.left = pre
        #     pre = cur
        
        # first = head.right
        # first.left = cur
        # cur.right = first
    
        # return first
        
