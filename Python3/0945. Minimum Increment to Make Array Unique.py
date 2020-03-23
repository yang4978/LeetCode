class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(50000)

        res = 0
        taken = 0

        for i in range(1,len(A)):
            if A[i] == A[i-1]:
                res -= A[i]
                taken += 1
            else:
                inter = min(A[i]-A[i-1]-1,taken)
                res += (A[i-1]+inter+A[i-1]+1)*inter//2
                taken -= inter
        
        return res

        # count = [0]*80000

        # for i in A:
        #     count[i] += 1
        
        # res = 0
        # taken = 0
        # for i in range(80000):
        #     if count[i] > 1:
        #         taken += count[i] - 1
        #         res -= (count[i]-1)*i
        #     elif taken and count[i] == 0:
        #         res += i
        #         taken -= 1
        
        # return res
