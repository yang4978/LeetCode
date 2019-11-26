class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        bad = [0]*n
        for i in range(n):
            left = (i-A[i]+1+n)%n
            right = (i+1)%n

            bad[left] += 1
            bad[right] -= 1

            if left>right:
                bad[0] += 1
            
        res = -n
        ans = 0
        temp = 0
        for i in range(n):
            temp -= bad[i]
            if temp>res:
                res = temp
                ans = i
        
        return ans
