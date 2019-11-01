class Solution:
    def countDigitOne(self, n: int) -> int:
        i = 1
        res = 0
        while(i<=n):
            res += n//(i*10)*i + max(0,min(n%(i*10)-i+1,i))
            i *= 10
        return res
