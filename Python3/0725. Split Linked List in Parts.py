# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        node = root
        h = 0
        while node:
            node = node.next
            h += 1
        
        n = h//k
        t = h%k

        node = root
        res = []

        while k>=1:
            res.append(node)
            tt = 1

            if t:
                tt = 0
                t -= 1

            while tt<n:
                node = node.next
                tt += 1
            
            if node:
                ll = node.next
                node.next = None
                node = ll


            k -= 1

        return res
