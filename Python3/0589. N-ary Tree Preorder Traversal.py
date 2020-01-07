"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        
        return res


    # def traversal(self,root):
    #     if not root:
    #         return
    #     self.res.append(root.val)
        
    #     for child in root.children:
    #         self.traversal(child)

    # def preorder(self, root: 'Node') -> List[int]:
    #     self.res = []
    #     self.traversal(root)
    #     return self.res
