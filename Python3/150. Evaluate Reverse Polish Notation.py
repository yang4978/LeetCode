class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ["+","-","*","/"]:
                temp = int(c)
                stack.append(temp)
            else:
                temp = stack.pop()
                if c == '+':
                    stack[-1] += temp
                elif c == '-':
                    stack[-1] -= temp
                elif c == '/':
                    flag = 1
                    if(stack[-1]<0 and temp>0) or (stack[-1]>0 and temp<0):
                        flag = -1
                    stack[-1] = abs(stack[-1])//abs(temp)*flag
                else:
                    stack[-1] *= temp
                temp = 0

        return stack[-1]
