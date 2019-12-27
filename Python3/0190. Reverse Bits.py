class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # mask = 1
        # res = 0
        # for i in range(32):
        #     res = res*2 + (mask&n!=0)
        #     mask <<= 1
        # return res
        print(bin(n))
        return int(bin(n)[:1:-1],2)
