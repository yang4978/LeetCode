class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tree = preorder.split(',')
        stack = [1]
        for s in tree:
            if not stack:
                return False

            stack[-1] -= 1
            if stack[-1] == 0:
                stack.pop()

            if s.isdigit():
                stack.append(2)
            
        return True if not stack else False
