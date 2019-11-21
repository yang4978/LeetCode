class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [i**2 for i in A]
        res.sort()
        return res
        # res = []
        # j = 0

        # while j<len(A) and A[j]<0:
        #     j += 1
        # i = j-1

        # while(i>=0 and j<len(A)):
        #     if(A[i]**2<A[j]**2):
        #         res.append(A[i]**2)
        #         i -= 1
        #     else:
        #         res.append(A[j]**2)
        #         j += 1
        
        # while(i>=0):
        #     res.append(A[i]**2)
        #     i -= 1
        
        # while(j<len(A)):
        #     res.append(A[j]**2)
        #     j += 1
        
        # return res

        # res = []
        # i,j = 0, len(A)-1
        # a = A[i]**2
        # b = A[j]**2
        # while(i<=j):
        #     if(a>b):
        #         res.append(a)
        #         i += 1
        #         a = A[i]**2
        #     else:
        #         res.append(b)
        #         j -= 1
        #         b = A[j]**2
        
        # return res[::-1]
