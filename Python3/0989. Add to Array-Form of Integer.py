class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        flag = 0
        for i in range(len(A)-1,-1,-1):
            A[i],flag = (A[i]+K%10+flag)%10, (A[i]+K%10+flag)//10
            K = K//10
        
        while flag or K:
            A = [0]+A
            A[0],flag = (K%10+flag)%10,(K%10+flag)//10
            K = K//10
        
        return A
