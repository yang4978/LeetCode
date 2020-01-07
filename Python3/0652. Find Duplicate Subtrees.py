# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def traversal(self,root):
        # if not root:
        #     return '#'
        
        # s = str(root.val)+","+self.traversal(root.left)+","+self.traversal(root.right)

        if not root:
            return ""
        
        if not root.left and not root.right:
            s = str(root.val)
        
        elif not root.right:
            s = str(root.val)+'('+self.traversal(root.left)+')'
        
        else:
            s = str(root.val)+'('+self.traversal(root.left)+')'+'('+self.traversal(root.right)+')'

        if s not in self.node_list:
            self.node_list[s] = 1
        elif self.node_list[s] == 1:
            self.ans.append(root)
            self.node_list[s] += 1
        
        return s

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.node_list = {}
        self.ans = []
        self.traversal(root)

        return self.ans
