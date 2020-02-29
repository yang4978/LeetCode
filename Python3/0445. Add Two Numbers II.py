# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def list_length(self,head):
        if not head:
            return 0
        
        else:
            return 1 + self.list_length(head.next)
    
    def add_node(self,h1,h2,flag):
        if not h1:
            return None,0

        h1.next, flag = self.add_node(h1.next,h2.next,flag)
        h1.val, flag = (h1.val+h2.val+flag)%10, (h1.val+h2.val+flag)//10

        return h1,flag

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len_1 = self.list_length(l1)
        len_2 = self.list_length(l2)

        h1 = ListNode(0)
        cur1 = h1
        h2 = ListNode(0)
        cur2 = h2


        if len_1 > len_2:
            k = len_1 - len_2

            while k:
                cur2.next = ListNode(0)
                cur2 = cur2.next
                k -= 1
        
        else:
            k = len_2 - len_1
            while k:
                cur1.next = ListNode(0)
                cur1 = cur1.next
                k -= 1
        
        cur1.next = l1
        cur2.next = l2

        h1,flag = self.add_node(h1,h2,0)

        return h1 if h1.val else h1.next


    # def list_reverse(self,head):
    #     if not head:
    #         return head
        
    #     new_head = None
    #     cur = head

    #     while cur:
    #         t = cur.next
    #         cur.next = new_head
    #         new_head = cur
    #         cur = t
        
    #     return new_head

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     l1 = self.list_reverse(l1)
    #     l2 = self.list_reverse(l2)
    #     flag = 0
    #     cur1 = l1
    #     cur2 = l2
    #     pre = cur1

    #     while cur1 and cur2:
    #         pre = cur1
    #         cur1.val, flag = (cur1.val+cur2.val +flag)%10, (cur1.val+cur2.val +flag)//10
    #         cur1 = cur1.next
    #         cur2 = cur2.next
        

    #     if not cur1 and cur2:
    #         pre.next = cur2
    #         cur1 = pre.next

    #     while cur1:
    #         pre = cur1
    #         cur1.val, flag = (cur1.val+flag)%10, (cur1.val+flag)//10
    #         cur1 = cur1.next

    #     if flag:
    #         pre.next = ListNode(1)
        
    #     return self.list_reverse(l1)
        
