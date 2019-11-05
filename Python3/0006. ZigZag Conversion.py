class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows<2): return s
        res = [""]*numRows
        index = 0
        flag = 1
        for i in s:
            res[index] += i
            index += flag
            if(index==numRows-1 or index==0):
                flag = -flag
        return ''.join(res)
#         l = len(s)
#         if(numRows>=l):return s
#         if(numRows==1):return s
#         res = ''
#         j = 0
#         while(j<numRows):
#             for i in range(0,l+numRows,2*numRows-2):
#                 if(i-j>=0 and i-j<l):
#                     res += s[i-j]
#                 if(i+j<l and j!=0 and j!=numRows-1):
#                     res += s[i+j]
#             j += 1
        
#         return res
