# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self,head,k):
        i = 0
        new_head = None
        while(i<k and head):
            if i==0:
                end = head
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
            i += 1
        end.next = temp
        return new_head if i==k else self.reverse(new_head,i)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node.next:
            node.next = self.reverse(node.next,k)
            m = 0
            while node and m<k:
                node=node.next
                m += 1
            if node == None:
                break
        return dummy.next
    
