class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcd_ab = a*b//math.gcd(a,b)
        lcd_ac = a*c//math.gcd(a,c)
        lcd_bc = b*c//math.gcd(b,c)
        lcd = lcd_ab*c//math.gcd(lcd_ab,c)

        left = 1
        right = min(a,b,c)*n

        while left<right:
            mid = (left+right)//2
            if mid//a + mid//b + mid//c - mid//lcd_ab - mid//lcd_ac - mid//lcd_bc + mid//lcd < n:
                left = mid+1
            else:
                right = mid
        
        return left
