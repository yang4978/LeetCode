# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        rhead = None

        while fast and fast.next:
            fast = fast.next.next
            t = slow.next
            slow.next = rhead
            rhead = slow
            slow = t
        
        if fast:
            slow = slow.next
        
        while slow and rhead:
            if slow.val != rhead.val:
                return False    
            slow = slow.next
            rhead = rhead.next
        
        return True

