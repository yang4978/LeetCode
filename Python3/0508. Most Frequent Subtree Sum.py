# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        number = collections.defaultdict(int)
        
        def treeSum(root):
            if not root:
                return 0
            res = root.val + treeSum(root.left) + treeSum(root.right)
            number[res] += 1
            return res
        
        treeSum(root)

        if not number:
            return []

        max_time = max(number.values())
        return [key for key,value in number.items() if value == max_time]
