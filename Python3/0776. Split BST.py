# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None,None]
        elif root.val>V:
            temp = self.splitBST(root.left,V)
            root.left = temp[1]
            return [temp[0],root]
        else:
            temp = self.splitBST(root.right, V)
            root.right = temp[0]
            return [root,temp[1]]

