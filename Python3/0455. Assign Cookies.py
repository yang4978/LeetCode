class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=j=res=0
        while(i<len(s) and j<len(g)):
            if(s[i]>=g[j]):
                res += 1
                j += 1
            i += 1
        return res
        
#         g.sort()
#         s.sort()
#         res = 0
#         j = len(g)-1
#         i = len(s)-1
        
#         while(i>=0 and j>=0):
#             if(s[i]>=g[j]):
#                 res += 1
#                 i -= 1
#             j -= 1
#         return res
