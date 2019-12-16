# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res==res[::-1]

###先找中点，后翻转####
        if not head:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        fast = slow.next
        dummy = ListNode(-1)

        while fast:
            after = fast.next
            fast.next = dummy.next
            dummy.next = fast
            fast = after
        
        node = dummy.next
        while head and node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        
        return True

####一边找中点，一边翻转####

        # if not head or not head.next:
        #     return True
        # slow = head
        # after = head
        # fast = head
        # dummy = ListNode(-1)

        # while fast.next and fast.next.next:
        #     fast = fast.next.next                
        #     after = slow.next
        #     slow.next = dummy.next
        #     dummy.next = slow
        #     slow = after  

        # last_half = after.next

        # if fast.next:
        #     after = slow.next
        #     slow.next = dummy.next
        #     dummy.next = slow
        #     slow = after  

        # node = dummy.next

        # while last_half and node:
        #     if last_half.val != node.val:
        #         return False
        #     last_half = last_half.next
        #     node = node.next
        
        # return True
