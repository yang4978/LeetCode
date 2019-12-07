# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head:
            prev = head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
        
            root = TreeNode(slow.val)
            root.right = self.sortedListToBST(slow.next)
           
            if head==slow:
                head = None
            else:
                prev.next = None
            root.left = self.sortedListToBST(head)

            return root

        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        
        # def helper(nums):
        #     if nums:
        #         l = len(nums)
        #         i = l//2
        #         root = TreeNode(nums[i])
        #         root.left = helper(nums[:i])
        #         root.right = helper(nums[i+1:])
        #         return root
        # return helper(arr)
