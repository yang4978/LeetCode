# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0: return []

        def partition(arr):
            res = []
            if arr == []:
                return [None]
                
            if len(arr) == 1:
                return [TreeNode(arr[0])]

            for k in range(len(arr)):
                for left in partition(arr[:k]):
                    for right in partition(arr[k+1:]):
                        node = TreeNode(arr[k])
                        node.left = left
                        node.right = right
                        res.append(node)
            return res

        return partition([i for i in range(1,n+1)])
