# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        root = node.right
        
        while root:
            self.stack.append(root)
            root = root.left


        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0

# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         def visitAllLeft(stack):
#             while stack[-1].left:
#                 stack.append(stack[-1].left)
#         self.num = []
#         if root:
#             stack = [root]
#             visitAllLeft(stack)

#             while stack:
#                 node = stack.pop()
#                 self.num.append(node.val)

#                 if node.right:
#                     stack.append(node.right)
#                     visitAllLeft(stack)

#         self.smallest = 0
        

#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         self.smallest += 1
#         return self.num[self.smallest-1]

#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return self.smallest<len(self.num)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
