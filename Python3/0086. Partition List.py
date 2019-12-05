# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = ListNode(-1)
        r1 = h1
        h2 = ListNode(-1)
        r2 = h2

        node = head
        while node:
            if node.val<x:
                h1.next = node
                h1 = h1.next
            else:
                h2.next = node
                h2 = h2.next
            node = node.next

        h2.next = None
        h1.next = r2.next

        return r1.next
        
        
