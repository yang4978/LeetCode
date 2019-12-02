class Solution:
    def isHappy(self, n: int) -> bool:
        def calSquare(num):
            res = 0
            while num:
                res += (num%10)**2
                num //= 10
            return res
        
        slow = n
        slow = calSquare(slow)
        fast = n
        fast = calSquare(fast)
        fast = calSquare(fast)

        while slow!=fast:
            slow = calSquare(slow)
            fast = calSquare(fast)
            fast = calSquare(fast)
        
        return slow==1

        # num = set()
        # while n!=1:
        #     t = n
        #     temp = 0
        #     while t:
        #         temp += (t%10)**2
        #         t //= 10
        #     if temp in num:
        #         return False
        #     else:
        #         n = temp
        #         num |= {temp}
        
        # return True
