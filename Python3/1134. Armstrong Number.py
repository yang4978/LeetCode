class Solution:
    def isArmstrong(self, N: int) -> bool:
        d = 1
        div = 10

        while N % div != N:
            d += 1
            div *= 10
        
        temp = 0
        num = N
        div //= 10

        while N:
            temp += (N%10)**d
            N //= 10

        return temp == num
