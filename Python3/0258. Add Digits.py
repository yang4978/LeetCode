class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num else num
        # while num>9:
        #     temp = 0
        #     while num:
        #         temp += num%10
        #         num //= 10
        #     num = temp

        # return num
