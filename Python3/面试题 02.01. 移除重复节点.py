# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre = head
        node = head
        num = set()

        while node:
            if node.val not in num:
                num.add(node.val)
                pre = node
            else:
                pre.next = node.next

            node = node.next
        
        return head
