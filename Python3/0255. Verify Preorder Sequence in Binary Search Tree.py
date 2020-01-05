class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        curMax = -float('inf')
        for n in preorder:
            while stack and stack[-1]<n:
                curMax = stack.pop()
            if n<curMax:
                return False
            stack.append(n)
        
        return True
