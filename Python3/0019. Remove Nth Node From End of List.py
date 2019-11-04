# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        temp1 = dummy
        temp2 = dummy
        
        while(n!=0):
            temp2 = temp2.next
            n -= 1
        
        while(temp2.next):
            temp1 = temp1.next
            temp2 = temp2.next
        
        temp1.next = temp1.next.next
        
        return dummy.next
        
#         layer = 0
#         temp = head
        
#         while(temp):
#             layer += 1
#             temp = temp.next
        
#         if(layer==n):
#             return head.next
        
#         temp = head
#         t_layer = layer-n-1
#         while(t_layer>0):
#             temp = temp.next
#             t_layer -= 1
#         if(temp.next):
#             temp.next = temp.next.next
        
#         return head
