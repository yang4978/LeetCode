# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB

        while l1 and l2:
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            headA = headA.next
            l1 = l1.next
        
        while l2:
            headB = headB.next
            l2 = l2.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
