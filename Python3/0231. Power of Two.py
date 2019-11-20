class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
        # if(n<=0):
        #     return False
        # mask = 1
        # res = 0
        # for i in range(32):
        #     if mask&n:
        #         if res:
        #             return False
        #         else:
        #             res = 1
        #     mask <<= 1
        # return res==1
