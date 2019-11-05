class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for i in lists:
            while i:
                temp.append(i.val)
                i = i.next
        
        temp.sort()
        
        dummy = ListNode(0)
        head = dummy
        for i in temp:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next
