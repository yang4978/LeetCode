class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i in num1:
            temp = 0
            for j in num2:
                temp = temp*10 + int(i)*int(j)
            res = res*10 + temp
        return str(res)
