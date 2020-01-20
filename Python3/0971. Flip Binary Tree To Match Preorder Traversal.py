# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # self.i = 0
        # self.res = []

        # def dfs(node):
        #     if not node:
        #         return
        #     if node.val != voyage[self.i]:
        #         self.res = [-1]
        #         return
            
        #     self.i += 1
        #     if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
        #         self.res.append(node.val)
        #         dfs(node.right)
        #         dfs(node.left)
        #     else:
        #         dfs(node.left)
        #         dfs(node.right)
        
        # dfs(root)

        # return self.res

        res,stack = [],[]
        i = 0
        pre = TreeNode(-1)
        
        while root:
            if root.val == voyage[i]:
                i += 1
                stack.append(root)
                pre = root
                root = root.left
            elif not pre.right or (pre.right and pre.right.val == voyage[i]):
                    res.append(pre.val)
                    root = pre.right
                    pre.right = pre.left
            else:
                return [-1]

        while stack:
            pre = stack.pop()
            node = pre.right
            while node:
                if node.val == voyage[i]:
                    i += 1
                    stack.append(node)
                    pre = node
                    node = node.left
                elif (not pre.right) or (pre.right and pre.right.val==voyage[i]):
                    res.append(pre.val)
                    node = pre.right
                    pre.right = pre.left
                else:
                    return [-1]
        return res
