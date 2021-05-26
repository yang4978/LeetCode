class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        last = []

        for c in s:
            if c != ')':
                stack.append(c)
            else:
                temp = []
                t = stack.pop()
                while(t != '('):
                    temp.append(t)
                    t = stack.pop()
                stack += temp
        
        return ("").join(stack)
