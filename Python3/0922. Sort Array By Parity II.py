class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        temp = -1
        for i in range(len(A)):
            if i%2 == 1 and A[i]%2 == 0:
                odd.append(i)
            elif i%2 == 0 and A[i]%2 == 1:
                even.append(i)
        
        for i in range(len(odd)):
            x = odd[i]
            y = even[i]
            A[x],A[y] = A[y],A[x]
        
        return A
