class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square = set()

        for i in range(int(c**0.5)+1):
            square.add(i*i)
            if (c - i*i) in square:
                return True
        
        return False
