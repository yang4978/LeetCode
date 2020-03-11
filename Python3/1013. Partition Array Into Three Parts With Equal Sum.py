class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        aver = sum(A)
        if aver%3:
            return False
        
        aver //= 3
        l = len(A)

        i = 1
        j = l - 2
        left = A[0]
        right = A[-1]

        while i<=j:
            if left == aver and right == aver:
                return True

            if left != aver:
                left += A[i]
                i += 1

            if right != aver:
                right += A[j]
                j -= 1
            
        return False    
