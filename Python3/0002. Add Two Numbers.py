# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        res = l3
        while(l1 or l2):
            if(l1):
                l3.val = l3.val+l1.val
                l1 = l1.next
            if(l2):
                l3.val = l3.val+l2.val
                l2 = l2.next
            if(l1 or l2 or l3.val>=10):
                l3.next = ListNode(l3.val//10)
                l3.val = l3.val%10
                l3 = l3.next
        return res
#         h1 = l1
#         h2 = l2
#         layer1,layer2 = 0,0
#         while(h1.next):
#             layer1 += 1
#             h1 = h1.next
#         while(h2.next):
#             layer2 += 1
#             h2 = h2.next
            
#         if(layer1>layer2):
#             for i in range(layer1-layer2):
#                 h2.next = ListNode(0)
#                 h2 = h2.next
#         else:
#             for i in range(layer2-layer1):
#                 h1.next = ListNode(0)
#                 h1 = h1.next
        
#         h1 = l1
#         h2 = l2
#         flag = 0
        
#         temp = flag + h1.val + h2.val
#         h1.val, flag = temp%10,temp//10  
        
#         while(h1.next!=None and h2.next!=None):
#             h1 = h1.next
#             h2 = h2.next
#             temp = flag + h1.val + h2.val
#             h1.val, flag = temp%10,temp//10  


#         if(flag):
#             h1.next = ListNode(flag)
#         return l1
