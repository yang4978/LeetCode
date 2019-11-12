# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy = ListNode(0)
        # head = dummy

        # while(l1 and l2):
        #     if l1.val<l2.val:
        #         head.next = l1
        #         l1 = l1.next
        #     else:
        #         head.next = l2
        #         l2 = l2.next
        #     head = head.next

        # if(l1!=None):
        #     head.next = l1

        # if(l2!=None):
        #     head.next = l2

        # return dummy.next
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        if(l1.val<l2.val):
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
        
