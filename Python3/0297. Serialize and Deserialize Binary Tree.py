# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def postorder(root):
            return [root.val] + postorder(root.left) + postorder(root.right) if root else ['#']
        
        return ' '.join(map(str, postorder(root)))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = iter(data.split())
        def helper():
            tmp = next(d)
            if tmp == "#":return 
            node = TreeNode(int(tmp))
            node.left = helper()
            node.right = helper()
            return node
        return helper()


        # preorder = list(data.split())

        # if preorder == "":
        #     return None

        # if preorder[0]!='#':
        #     head = TreeNode(int(preorder.pop(0))) 
        # else:
        #     return None
        # stack = [[head,0,0]]


        # while preorder:
        #     c = preorder.pop(0)
        #     while 1:
        #         node,left_flag,right_flag = stack[-1]
        #         if left_flag == 0:
        #             l = TreeNode(int(c)) if c!='#' else None
        #             node.left = l
        #             stack[-1][1] = 1
        #             if l:
        #                 stack.append([l,0,0])
        #             break
        #         elif right_flag == 0:
        #             r = TreeNode(int(c)) if c!='#' else None
        #             node.right = r
        #             stack[-1][2] = 1
        #             if r:
        #                 stack.append([r,0,0])
        #             break
        #         else:
        #             stack.pop()
    
        # return head



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
