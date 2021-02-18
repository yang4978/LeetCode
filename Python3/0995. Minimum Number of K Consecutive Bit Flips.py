class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res = 0
        length = len(A)
        diff = [0]*(length+1)
        rev_count = 0

        for i in range(length):
            rev_count += diff[i]
            if(A[i]+rev_count)%2 == 0:
                if i+K>length:
                    return -1
                res += 1
                rev_count += 1
                diff[i+K] -= 1
        
        return res
