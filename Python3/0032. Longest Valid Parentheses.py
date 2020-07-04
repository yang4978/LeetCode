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

        

#         def findValidParentheses(string,flag):
#             left, right = 0, 0
#             count = 0
#             res = 0

#             for i in string:
#                 if i == '(':
#                     left += 1

#                 elif i == ')':
#                     right += 1
                
#                 count += 1

#                 if left*flag < right*flag:
#                     left, right = 0, 0
#                     count = 0
                
#                 elif left == right:
#                     res = max(res,count)
            
#             return res
        
#         return max(findValidParentheses(s,1),findValidParentheses(reversed(s),-1))
