class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==""): return []
        letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = ['']
        for i in digits:
            res = [x+y for x in res for y in letter[i]]
        return res
        
        
#         if(digits==""): return []
        
#         letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
#         res = []
#         temp = ''
#         def dfs(i,temp):
#             if i == n:
#                 res.append(temp)
#                 return
#             for k in (letter[digits[i]]):
#                 tt = temp[:]
#                 temp += k
#                 dfs(i+1,temp)
#                 temp = tt[:]
        
#         n = len(digits)
#         dfs(0,temp)
        
#         return(res)
