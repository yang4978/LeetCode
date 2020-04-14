# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        queue = [tree]
        res = []
        while queue:
            head = ListNode(-1)
            temp = head
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.next = ListNode(node.val)
                temp = temp.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(head.next)
        return res
