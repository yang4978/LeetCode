class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        dp = [0]*(l+1)
        for i in range(1,l):
            if(s[i]==')'):
                if s[i-1]=='(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1] + 2
                    dp[i] += dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0
        return max(dp)


        # stack = [-1]
        # res = 0
        # for i in range(len(s)):
        #     if s[i]=='(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if stack:
        #             res = max(res,i-stack[-1])
        #         else:
        #             stack.append(i)

        # return res
