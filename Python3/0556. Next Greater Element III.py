class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # stack = []
        # res = 0
        # a = []
        # l = 0

        # while n:
        #     a.append(n%10)
        #     n = n//10
        #     l += 1
        # a.reverse()

        # for i in range(l-1,-1,-1):
        #     if stack and stack[-1]>a[i]:
        #         for j in range(len(stack)):
        #             if stack[j]>a[i]:
        #                 stack[j],a[i] = a[i],stack[j]
        #                 break

        #         a = a[:i]+[a[i]]+stack
        
        #         for i in range(l):
        #             n = n*10 + a[i]
        #         return n if n<=2**31-1 else -1
        #     stack.append(a[i])
        
        # return -1


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
        
        return -1
