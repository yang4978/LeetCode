"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        
        return res[::-1]

        # if not root:
        #     return []
        # stack = []
        # lists = [root]

        # res = []

        # while lists:
        #     node = lists.pop()
        #     stack.append(node)
        #     lists.extend(node.children)

        # while stack:
        #     res.append(stack.pop().val)    
        
        # return res

    # def traversal(self,root):
    #     if not root:
    #         return
    #     for child in root.children:
    #         self.traversal(child)
    #     self.res.append(root.val)    
        
    # def postorder(self, root: 'Node') -> List[int]:
    #     self.res = []
    #     self.traversal(root)
    #     return self.res
