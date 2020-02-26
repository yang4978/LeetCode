# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if not head or k<=0:
            return None

        slow = head
        fast = head
        
        for i in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.val

        # length = 1
        # node = head
        # while node:
        #     node = node.next
        #     length += 1
        
        # n = length - k - 1

        # while n:
        #     head = head.next
        #     n -= 1
        
        # return head.val
