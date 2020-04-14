class Solution:
    def waysToStep(self, n: int) -> int:
        pp = 0
        pre = 0
        cur = 1

        while n:
            pp, pre, cur = pre, cur,(pp + pre + cur)%1000000007
            n -= 1
        return cur
