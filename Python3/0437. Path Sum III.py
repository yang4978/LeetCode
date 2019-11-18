# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        stack = [(root,[root.val])]
        res = 0

        while stack:
            node,temp = stack.pop()
            res += temp.count(sum)
            temp += [0]
            if node.left:
                arr = [i+node.left.val for i in temp]
                stack.append((node.left,arr))
            
            if node.right:
                arr = [i+node.right.val for i in temp]
                stack.append((node.right,arr))
        
        return res
