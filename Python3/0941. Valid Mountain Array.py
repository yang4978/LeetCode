class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
            
        index = A.index(max(A))

        if index == 0 or index == len(A)-1:
            return False

        for i in range(index):
            if A[i] >= A[i+1]:
                return False
        
        for i in range(index,len(A)-1):
            if A[i] <= A[i+1]:
                return False
        
        return True
