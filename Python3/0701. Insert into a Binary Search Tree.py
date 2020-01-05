# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insert(self,root,val):
        if val<root.val:
            if not root.left:
                root.left = TreeNode(val)
                return
            else:
                self.insertIntoBST(root.left,val)
        
        else:
            if not root.right:
                root.right = TreeNode(val)
                return
            else:
                self.insertIntoBST(root.right,val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.insert(root,val)
        return root
