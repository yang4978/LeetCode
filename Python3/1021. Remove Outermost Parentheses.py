class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = ""
        res = ""
        l = 0
        
        for i in S:
            if i==')':
                l -= 1

            if l!=0:
                res += i

            if i=='(':
                l += 1
            
        return res


        # stack = ""
        # res = ""
        # l = 0
        
        # for i in S:
        #     if i=='(':
        #         l += 1
        #     else:
        #         l -= 1
            
        #     if l==0:
        #         res += stack[1:]
        #         stack = ""
        #         l = 0
        #     else:
        #         stack += i
        
        # return res
