class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(T))
        for i in range(len(T)-1,-1,-1):
            while stack and T[stack[-1]]<=T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]-i
            stack.append(i)
        return res
    
        # l = len(T)
        # temp = {}
        # for i in range(102):
        #     temp[i] = l+1
        # ans = [0]*l
        # for i in range(l-1,-1,-1):
        #     x = min([temp[k] for k in range(T[i]+1,102)])
        #     if(x!=l+1):
        #         ans[i] = x-i
        #     temp[T[i]] = i
        # return ans
