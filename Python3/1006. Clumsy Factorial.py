class Solution:
    def clumsy(self, N: int) -> int:
        flag = 0
        result = 0
        rest = N % 4
        temp = 0

        for i in range(N, 0, -1):
            if i%4 == rest:
                temp = i
            elif i%4 == rest - 1 or i%4 == rest + 3:
                temp *= i
            elif i%4 == rest - 2 or i%4 == rest + 2:
                temp //= i
            else:
                if(flag == 0):
                    result = temp
                    flag = 1
                else:
                    result += flag * temp
                    flag = - flag
                result += flag * i
                flag = - flag
                temp = 0

        if flag == 0:
            flag = 1

        return result + flag * temp
