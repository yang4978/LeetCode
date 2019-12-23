class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag = 0
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                flag = flag
            elif A[i]>A[i-1] and flag>=0:
                flag = 1
            elif A[i]<A[i-1] and flag<=0:
                flag = -1
            else:
                return False
        
        return True
