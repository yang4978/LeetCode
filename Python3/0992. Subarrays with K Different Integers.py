class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        l = len(A)
        res = 0
        total1 = 0
        total2 = 0
        num1 = collections.defaultdict(int)
        num2 = collections.defaultdict(int)
        left1 = 0
        left2 = 0

        for right in range(l):
            n = A[right]

            if num1[n] == 0:                
                total1 += 1
            if num2[n] == 0:
                total2 += 1

            num1[n] += 1
            num2[n] += 1
            
            while total1 > K-1:
                num1[A[left1]] -= 1
                if num1[A[left1]] == 0:
                    total1 -= 1
                left1 += 1
            
            while total2 > K:
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    total2 -= 1
                left2 += 1
            
            res += left1 - left2
        
        return res
