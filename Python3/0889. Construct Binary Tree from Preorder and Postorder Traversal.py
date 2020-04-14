# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    #     stack = [TreeNode(-1)]
    #     l = len(post)
    #     i = 0
    #     j = 0

    #     while i<l:
    #         while stack[-1].val == post[j]:
    #             stack.pop()
    #             j += 1

    #         node = TreeNode(pre[i])
    #         if not stack[-1].left:
    #             stack[-1].left = node
    #         else:
    #             stack[-1].right = node
    #         stack.append(node)
    #         i += 1

    #     return stack[0].left



    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        i = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:i+2],post[:i+1])
        root.right = self.constructFromPrePost(pre[i+2:],post[i+1:-1])

        return root
