class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 0
        div = 5
        while div <= n:
            five += n//div
            div *= 5
        
        return five
