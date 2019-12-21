class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        l = [0]*n

        stack = [-1]
        for i in range(n):
            while stack[-1]!=-1 and A[stack[-1]]>A[i]:
                stack.pop()
            l[i] = stack[-1]
            stack.append(i)
        
        stack = [n]
        for i in range(n-1,-1,-1):
            while stack[-1]!=n and A[stack[-1]]>=A[i]:
                stack.pop()
            res += A[i]*(i-l[i])*(stack[-1]-i)
            #res = (res+(A[i]*(i-l[i])*(stack[-1]-i))%(10**9+7))%(10**9+7)
            stack.append(i)
        
        return res%(10**9+7)
