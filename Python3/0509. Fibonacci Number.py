class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0

        pre = 0
        cur = 1

        while N-1:
            pre, cur = cur, pre + cur
            N -= 1
        
        return cur
