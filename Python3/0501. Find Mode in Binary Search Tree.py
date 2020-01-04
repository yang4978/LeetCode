# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        num = collections.defaultdict(int)

        def visit(root):
            if not root:
                return
            num[root.val] += 1
            visit(root.left)
            visit(root.right)
        
        visit(root)

        max_times = max(num.values())
        
        return [i for i in num if num[i]==max_times]
