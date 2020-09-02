# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1 = headA
        h2 = headB
        l1 = h1
        l2 = h2

        while l1 and l2:
            l1 = l1.next
            l2 = l2.next
        
        if l2:
            l1, l2 = l2, l1
            h1, h2 = h2, h1
        
        l2 = h1
        while l1:
            l1 = l1.next
            l2 = l2.next
            
        l1 = h2

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        
        return l2
