# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list(self,head):
        if not head:
            return head
        
        temp = head
        new_head = None

        while temp:
            tt = temp.next
            temp.next = new_head
            new_head = temp
            temp = tt
        
        return new_head


    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = self.reverse_list(slow.next)
        slow.next = None

        while l2 != None:
            t = l2.next
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
            l2 = t
            
        return head
