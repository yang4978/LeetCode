class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        stack = []
        res = ''
        for i in self.countAndSay(n-1):
            if stack and i!=stack[-1]:
                res += str(len(stack))+stack[-1]
                stack=[]
            stack.append(i)
        if stack:
            res += str(len(stack))+stack[-1]
        return res
