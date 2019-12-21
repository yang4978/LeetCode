class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = []
        res = 0

        while n:
            t = n%10
            n = n//10
            if stack and stack[-1]>t:
                for i in range(len(stack)):
                    if stack[i]>t:
                        stack[i],t = t,stack[i]
                        break
                digit = 0
                while stack:
                    res = res*10 + stack.pop(0)
                    digit += 1
                n = n*pow(10,digit+1)+t*pow(10,digit)+res
                return n if n<=2**31-1 else -1
            stack.append(t)
            stack.sort()
        
        return -1
