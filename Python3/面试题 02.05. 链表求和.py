# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def cal(v1,v2,f):
            temp = v1 + v2 + f
            return temp%10, temp//10

        n1 = l1
        n2 = l2
        flag = 0

        while n1.next and n2.next:
            n1.val,flag = cal(n1.val,n2.val,flag)
            n1 = n1.next
            n2 = n2.next
        
        n1.val,flag = cal(n1.val,n2.val,flag)

        if n2.next:
            n1.next = n2.next

        if n1.next:
            n1 = n1.next
            while n1.next:
                n1.val,flag = cal(n1.val,0,flag)
                n1 = n1.next
                
            n1.val,flag = cal(n1.val,0,flag)
        if flag:
                n1.next = ListNode(flag)

        return l1    
