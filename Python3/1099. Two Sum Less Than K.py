class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        i,j = 0,len(A)-1
        res = -1
        A.sort()
        while i<j :
            if(A[i]+A[j]<K):
                if(A[i]+A[j]>res):
                    res = A[i]+A[j]
                i += 1
            else:
                j -= 1
        return res
