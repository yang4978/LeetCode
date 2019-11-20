class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n^(n>>1)
        return x&(x+1)==0
        # mask = 1
        # flag = -1
        # num = 0
        # while num<n:
        #     num += mask
        #     t = mask&n!=0
        #     if flag == t:
        #         return False
        #     else:
        #         flag = t
        #     mask <<= 1
        # return True
